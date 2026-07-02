from __future__ import annotations

import hashlib
import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
ENGINE = ROOT / "hg-engine-main"
PERFECT_ENGINE = ROOT.parent / "perfect_johto" / "hg-engine-main" / "hg-engine-main"

DOJO_SCRIPT = ENGINE / "armips" / "scr_seq" / "scr_seq_00832_phase8_dojo.s"
DOJO_TEXT = ENGINE / "data" / "text" / "533.txt"
ASSEMBLED_DOJO = ENGINE / "build" / "a012" / "2_832"

PHASE8_FLAGS = {
    "FLAG_PHASE8_CAUGHT_MEW": 2865,
    "FLAG_PHASE8_CAUGHT_CELEBI": 2866,
    "FLAG_PHASE8_CAUGHT_REGIROCK": 2867,
    "FLAG_PHASE8_CAUGHT_REGICE": 2868,
    "FLAG_PHASE8_CAUGHT_REGISTEEL": 2869,
    "FLAG_PHASE8_CAUGHT_REGIGIGAS": 2870,
    "FLAG_PHASE8_CAUGHT_LATIAS": 2871,
    "FLAG_PHASE8_CAUGHT_LATIOS": 2872,
    "FLAG_PHASE8_CAUGHT_JIRACHI": 2873,
    "FLAG_PHASE8_CAUGHT_DEOXYS": 2874,
    "FLAG_PHASE8_CAUGHT_UXIE": 2875,
    "FLAG_PHASE8_CAUGHT_MESPRIT": 2876,
    "FLAG_PHASE8_CAUGHT_AZELF": 2877,
    "FLAG_PHASE8_CAUGHT_DIALGA": 2878,
    "FLAG_PHASE8_CAUGHT_PALKIA": 2879,
    "FLAG_PHASE8_CAUGHT_GIRATINA": 2880,
    "FLAG_PHASE8_CAUGHT_HEATRAN": 2881,
    "FLAG_PHASE8_CAUGHT_CRESSELIA": 2882,
    "FLAG_PHASE8_CAUGHT_DARKRAI": 2883,
    "FLAG_PHASE8_CAUGHT_SHAYMIN": 2884,
    "FLAG_PHASE8_CAUGHT_MANAPHY": 2885,
    "FLAG_PHASE8_CAUGHT_PHIONE": 2886,
    "FLAG_PHASE8_CAUGHT_ARCEUS": 2887,
}

EXPECTED_DOSSIER_SPECIES = {
    "SPECIES_ARTICUNO",
    "SPECIES_ZAPDOS",
    "SPECIES_MOLTRES",
    "SPECIES_MEWTWO",
    "SPECIES_LUGIA",
    "SPECIES_HO_OH",
    "SPECIES_SUICUNE",
    "SPECIES_LATIAS",
    "SPECIES_LATIOS",
    "SPECIES_REGIROCK",
    "SPECIES_REGICE",
    "SPECIES_REGISTEEL",
    "SPECIES_REGIGIGAS",
    "SPECIES_KYOGRE",
    "SPECIES_GROUDON",
    "SPECIES_RAYQUAZA",
    "SPECIES_MEW",
    "SPECIES_CELEBI",
    "SPECIES_JIRACHI",
    "SPECIES_DEOXYS",
    "SPECIES_HEATRAN",
    "SPECIES_CRESSELIA",
    "SPECIES_DARKRAI",
    "SPECIES_SHAYMIN",
    "SPECIES_MANAPHY",
    "SPECIES_PHIONE",
    "SPECIES_UXIE",
    "SPECIES_MESPRIT",
    "SPECIES_AZELF",
    "SPECIES_DIALGA",
    "SPECIES_PALKIA",
    "SPECIES_GIRATINA",
    "SPECIES_ARCEUS",
}

CHAMPION_CIRCUIT_IDS = {
    260: (92, 96),
    727: (92, 96),
    733: (92, 96),
    738: (92, 96),
    739: (92, 96),
    740: (92, 96),
}


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="replace")


def file_hash(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def parse_flags() -> dict[str, int]:
    values: dict[str, int] = {}
    for line in read_text(ENGINE / "armips" / "include" / "flags.s").splitlines():
        match = re.match(r"(FLAG_[A-Z0-9_]+)\s+equ\s+(\d+)", line)
        if match:
            values[match.group(1)] = int(match.group(2))
    return values


def parse_species() -> set[str]:
    values: set[str] = set()
    for line in read_text(ENGINE / "asm" / "include" / "species.inc").splitlines():
        match = re.match(r"\.equ\s+(SPECIES_[A-Z0-9_]+),", line)
        if match:
            values.add(match.group(1))
    return values


def trainer_block(trainers: str, trainer_id: int) -> str:
    match = re.search(
        rf"(?ms)^    \[{trainer_id}\] = \{{.*?(?=^    \[\d+\] = \{{|^}};)",
        trainers,
    )
    if not match:
        raise AssertionError(f"trainer {trainer_id} block not found")
    return match.group(0)


def validate_trainer_block(trainers: str, trainer_id: int, min_level: int, max_level: int) -> list[str]:
    errors: list[str] = []
    block = trainer_block(trainers, trainer_id)
    species_count = len(re.findall(r"\.species\s*=\s*SPECIES_", block))
    levels = [int(level) for level in re.findall(r"\.level\s*=\s*(\d+)", block)]
    if species_count != 6:
        errors.append(f"trainer {trainer_id} has {species_count} Pokemon, expected 6")
    if not levels:
        errors.append(f"trainer {trainer_id} has no parsed levels")
    elif min(levels) != min_level or max(levels) != max_level:
        errors.append(
            f"trainer {trainer_id} levels are {min(levels)}-{max(levels)}, expected {min_level}-{max_level}"
        )
    return errors


def validate() -> list[str]:
    errors: list[str] = []

    if not DOJO_SCRIPT.exists():
        return [f"missing Dojo script: {DOJO_SCRIPT}"]
    if not DOJO_TEXT.exists():
        return [f"missing Dojo text archive: {DOJO_TEXT}"]

    script = read_text(DOJO_SCRIPT)
    flags = parse_flags()
    species = parse_species()
    trainers = read_text(ENGINE / "data" / "Trainers.c")

    for name, value in PHASE8_FLAGS.items():
        if flags.get(name) != value:
            errors.append(f"{name} is {flags.get(name)}, expected {value}")

    script_flags = set(re.findall(r"FLAG_[A-Z0-9_]+", script))
    missing_flags = sorted(flag for flag in script_flags if flag not in flags)
    if missing_flags:
        errors.append("script references missing flags: " + ", ".join(missing_flags))

    script_species = set(re.findall(r"SPECIES_[A-Z0-9_]+", script))
    missing_species = sorted(name for name in script_species if name not in species)
    if missing_species:
        errors.append("script references missing species: " + ", ".join(missing_species))

    dossier_species = set(re.findall(r"wild_battle\s+(SPECIES_[A-Z0-9_]+),", script))
    if dossier_species != EXPECTED_DOSSIER_SPECIES:
        errors.append(
            "dossier species mismatch: "
            + ", ".join(sorted(dossier_species.symmetric_difference(EXPECTED_DOSSIER_SPECIES)))
        )

    trainer_ids = {int(match) for match in re.findall(r"trainer_battle\s+(\d+),", script)}
    for trainer_id in sorted(trainer_ids):
        if not re.search(rf"(?m)^    \[{trainer_id}\] = \{{", trainers):
            errors.append(f"script references missing trainer {trainer_id}")

    for trainer_id, (min_level, max_level) in CHAMPION_CIRCUIT_IDS.items():
        errors.extend(validate_trainer_block(trainers, trainer_id, min_level, max_level))

    text_lines = read_text(DOJO_TEXT).splitlines()
    npc_message_ids = [int(match) for match in re.findall(r"npc_msg\s+(\d+)", script)]
    if npc_message_ids and max(npc_message_ids) >= len(text_lines):
        errors.append(f"text/533 has {len(text_lines)} lines, but script uses npc_msg {max(npc_message_ids)}")
    for phrase in ["Champion Circuit", "Kanto Legends", "Ancient Seals", "Creation Echoes"]:
        if phrase not in read_text(DOJO_TEXT):
            errors.append(f"text/533 is missing menu phrase: {phrase}")

    for trainer_id in [738, 739, 740]:
        if not re.search(rf"(?m)^    {trainer_id},$", trainers):
            errors.append(f"sTrainerTextOrder is missing Champion Circuit trainer {trainer_id}")

    perfect_assembled = PERFECT_ENGINE / "build" / "a012" / "2_832"
    if ASSEMBLED_DOJO.exists() and perfect_assembled.exists():
        current_hash = file_hash(ASSEMBLED_DOJO)
        perfect_hash = file_hash(perfect_assembled)
        if current_hash != perfect_hash:
            errors.append("assembled Dojo script hash does not match Perfect Johto reference")

    return errors


def main() -> int:
    errors = validate()
    if errors:
        print("Phase 6 postgame validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1

    print("Phase 6 postgame validation passed: Dojo hub, Champion Circuit, dossier references, and Phase 8 flags are valid.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
