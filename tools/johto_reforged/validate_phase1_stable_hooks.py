#!/usr/bin/env python3
"""Validate phase 1 UI/runtime rollback bytes and fragile text IDs."""

from __future__ import annotations

import argparse
import re
import struct
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
ENGINE = ROOT / "hg-engine-main"


ARM9_EV_IV_CLEAN_IF_DISABLED = [
    (0x02088B60, "20 21 DC 6C 26 1C 0E 42", "summary EV/IV viewer site"),
    (0x0208D2C4, "78 21 03 23 FF F7 D8 FA", "summary entry hook site"),
]


ARM9_EXPECTED = [
    (0x0208C848, "00 08 0E 00 00 07 0E 00", "summary stat colors"),
    (0x0208CDE8, "03", "summary dex digits"),
    (0x0207B0B0, "F0 B5 83 B0 01 91 3E 49", "party context setup A"),
    (0x0207AFC4, "38 B5 04 1C 81 20 80 00", "party context setup B"),
    (
        0x0207E28C,
        "F8 B5 88 B0 04 1C 00 20 05 90 50 1E 1D 1C 03 01 "
        "2B 4A 0E 98 04 91 C1 00",
        "party context text renderer",
    ),
    (
        0x0207E3A8,
        "F8 B5 88 B0 49 1E 0C 01 61 49 DB 00 09 19 59 18 "
        "51 56 05 1C 5F 48 89 00",
        "party context button renderer",
    ),
    (0x0207CB9C, "18 B4 C9 23 1B 01 C0 18", "party context button animation"),
    (
        0x020902B8,
        "38 B5 0D 1C 11 1C 1C 1C E4 F7 C0 F9",
        "party item-use can-use setup",
    ),
    (0x02081E54, "18 48 89 1E 20 58 61 5C", "party item-use learn-move loop"),
    (0x0208138C, "04 48 00 21 20 58 27 30", "party item-use repeat item"),
    (0x0207C288, "38 B5 05 1C 4C 48 00 21", "party item-use handler"),
    (0x0206E3C6, "01 F0 19 FD", "nature stat call attack"),
    (0x0206E406, "01 F0 F9 FC", "nature stat call defense"),
    (0x0206E446, "01 F0 D9 FC", "nature stat call speed"),
    (0x0206E486, "01 F0 B9 FC", "nature stat call special attack"),
    (0x0206E4C6, "01 F0 99 FC", "nature stat call special defense"),
    (0x0206FE3C, "08 B5 01 2A 01 D3 05 2A", "nature stat function"),
]


OVERLAY_EXPECTED = [
    (
        2,
        0x0224855C,
        "F8 B5 0D 1C 07 1C 68 7B 14 1C 1E 1C 00 28 04 D1 "
        "A8 7B 0E 28 01 D1 01 22",
        "wild post-processing hook site",
    ),
]


GENERATIONS_WILD_HOOK_CONFIG = "IMPLEMENT_GENERATIONS_WILD_MON_HOOK"


DEFERRED_WILD_HOOK_CONFIGS = {
    "IMPLEMENT_WILD_MON_POSTPROCESSING_HOOK",
    "RANDOM_LEGENDARY_ROAMING_ENCOUNTERS",
}


TEXT_EXPECTED = {
    40: [
        (26, "Would you like to save the game? {YESNO 0}", "save confirmation prompt"),
        (28, "There is already a saved file.\\nIs it OK to overwrite it? {YESNO 0}", "save overwrite prompt"),
        (30, "Saving...\\nDon’t turn off the power.", "save in-progress text"),
        (32, "{STRVAR_1 3, 0, 0} saved the game.", "save complete text"),
        (36, "Save error.", "save error text"),
        (40, "There is already a saved game file.\\nIt is impossible to save.\\rPlease refer to the Instruction\\nBooklet for details.\\rPress Up + SELECT + B Button on\\nthe title screen if you want to erase\\fthe current saved game file.", "save blocked text"),
        (42, "Saving a lot of data...\\nDon’t turn off the power.", "save large-data text"),
        (162, "Would you like to save the game?", "save screen prompt"),
        (164, "There is already a saved file.\\nIs it OK to overwrite it?", "save screen overwrite prompt"),
        (188, "Your Hall of Fame data is corrupted.\\rIt will be fixed if you enter the\\nHall of Fame again.\\r", "Hall of Fame corruption warning"),
        (234, "The repellent’s effect wore off!\\nWould you like to use another one?", "reusable Repel prompt"),
        (236, "You used the {STRVAR_1 8, 1, 0}.", "reusable Repel used text"),
        (238, "Begin auto-battle.", "debug auto-battle text"),
    ],
    197: [
        (1842, "What will {STRVAR_1 1, 0, 0} do?{YESNO 0}", "battle prompt"),
        (1848, "FIGHT", "battle command fight label"),
        (1850, "BAG", "battle command bag label"),
        (1852, "POKéMON", "battle command Pokemon label"),
        (1854, "RUN", "battle command run label"),
        (1862, "BALL", "Safari command ball label"),
        (1864, "BAIT", "Safari command bait label"),
        (1866, "MUD", "Safari command mud label"),
        (1874, "{STRVAR_1 51, 0, 0}/{STRVAR_1 51, 1, 0}", "battle move PP value"),
        (1876, "PP", "battle move PP label"),
        (1878, "Which move should\\nbe forgotten?", "battle move-forget prompt"),
        (1886, "Quit the battle?{YESNO 0}", "battle quit prompt"),
        (1900, "SAFARI BALLS", "Safari ball count label"),
        (1902, "Left: {STRVAR_1 51, 0, 0}", "Safari balls remaining label"),
    ],
    300: [
        (256, "SWITCH", "party menu switch command"),
        (258, "SUMMARY", "party menu summary command"),
        (260, "ITEM", "party menu item command"),
        (270, "QUIT", "party menu quit command"),
        (304, "FIRST", "party order first label"),
        (306, "SECOND", "party order second label"),
        (308, "THIRD", "party order third label"),
        (310, "FOURTH", "party order fourth label"),
        (312, "FIFTH", "party order fifth label"),
        (314, "SIXTH", "party order sixth label"),
        (316, "ABLE!", "party compatibility able label"),
        (318, "UNABLE!", "party compatibility unable label"),
    ],
    302: [
        (218, "SKILLS", "summary stat page title"),
        (220, "HP", "summary HP label"),
        (222, "Attack", "summary Attack label"),
        (224, "Defense", "summary Defense label"),
        (226, "Sp. Atk", "summary Sp. Atk label"),
        (228, "Sp. Def", "summary Sp. Def label"),
        (230, "Speed", "summary Speed label"),
        (232, "Ability", "summary Ability label"),
        (234, "/", "summary PP slash label"),
        (256, "BATTLE MOVES", "summary moves title"),
        (270, "PP", "summary PP label"),
        (292, "{ALN_CENTER}Cancel", "summary move cancel button"),
        (294, "POWER", "summary move power label"),
        (296, "ACCURACY", "summary move accuracy label"),
        (298, "CATEGORY", "summary move category label"),
        (304, "SWITCH", "summary move switch command"),
        (390, "HP", "summary EV/IV HP label"),
        (391, "Attack", "summary EV/IV Attack label"),
        (392, "Defense", "summary EV/IV Defense label"),
        (393, "Sp. Atk", "summary EV/IV Sp. Atk label"),
        (394, "Sp. Def", "summary EV/IV Sp. Def label"),
        (395, "Speed", "summary EV/IV Speed label"),
        (396, "Attack↑", "summary EV/IV Attack up label"),
        (397, "Defense↑", "summary EV/IV Defense up label"),
        (398, "Sp. Atk↑", "summary EV/IV Sp. Atk up label"),
        (399, "Sp. Def↑", "summary EV/IV Sp. Def up label"),
        (400, "Speed↑", "summary EV/IV Speed up label"),
        (401, "Attack↓", "summary EV/IV Attack down label"),
        (402, "Defense↓", "summary EV/IV Defense down label"),
        (403, "Sp. Atk↓", "summary EV/IV Sp. Atk down label"),
        (404, "Sp. Def↓", "summary EV/IV Sp. Def down label"),
        (405, "Speed↓", "summary EV/IV Speed down label"),
        (406, "EV", "summary EV mode label"),
        (407, "IV", "summary IV mode label"),
    ],
}


TEXT_COMPACT_EXPECTED = {
    302: [
        (109, "SKILLS", "runtime summary stat page title"),
        (110, "HP", "runtime summary HP label"),
        (111, "Attack", "runtime summary Attack label"),
        (112, "Defense", "runtime summary Defense label"),
        (113, "Sp. Atk", "runtime summary Sp. Atk label"),
        (114, "Sp. Def", "runtime summary Sp. Def label"),
        (115, "Speed", "runtime summary Speed label"),
        (116, "Ability", "runtime summary Ability label"),
        (117, "/", "runtime summary PP slash label"),
        (128, "BATTLE MOVES", "runtime summary moves title"),
        (135, "PP", "runtime summary PP label"),
        (146, "{ALN_CENTER}Cancel", "runtime summary move cancel button"),
        (147, "POWER", "runtime summary move power label"),
        (148, "ACCURACY", "runtime summary move accuracy label"),
        (149, "CATEGORY", "runtime summary move category label"),
        (152, "SWITCH", "runtime summary move switch command"),
        (195, "HP", "runtime summary EV/IV HP label"),
        (196, "Attack", "runtime summary EV/IV Attack label"),
        (197, "Defense", "runtime summary EV/IV Defense label"),
        (198, "Sp. Atk", "runtime summary EV/IV Sp. Atk label"),
        (199, "Sp. Def", "runtime summary EV/IV Sp. Def label"),
        (200, "Speed", "runtime summary EV/IV Speed label"),
        (201, "Attack↑", "runtime summary EV/IV Attack up label"),
        (202, "Defense↑", "runtime summary EV/IV Defense up label"),
        (203, "Sp. Atk↑", "runtime summary EV/IV Sp. Atk up label"),
        (204, "Sp. Def↑", "runtime summary EV/IV Sp. Def up label"),
        (205, "Speed↑", "runtime summary EV/IV Speed up label"),
        (206, "Attack↓", "runtime summary EV/IV Attack down label"),
        (207, "Defense↓", "runtime summary EV/IV Defense down label"),
        (208, "Sp. Atk↓", "runtime summary EV/IV Sp. Atk down label"),
        (209, "Sp. Def↓", "runtime summary EV/IV Sp. Def down label"),
        (210, "Speed↓", "runtime summary EV/IV Speed down label"),
        (211, "EV", "runtime summary EV mode label"),
        (212, "IV", "runtime summary IV mode label"),
    ],
}


SCRIPT_EXPECTED = {
    Path("armips/scr_seq/scr_seq_00003_commonscript.s"): [
        (
            r"scr_seq_0003_072_repels:.*?npc_msg 234.*?QueueNewRepel.*?npc_msg 236",
            "reusable Repel script uses appended bank 40 text IDs",
        ),
        (
            r"scr_seq_0003_073_autobattle_testing:.*?npc_msg 238",
            "debug auto-battle script uses appended bank 40 text ID",
        ),
    ],
}


SCRIPT_TEXT_BANKS = {
    Path("armips/scr_seq/scr_seq_00003_commonscript.s"): 40,
}


def parse_bytes(value: str) -> bytes:
    return bytes.fromhex(value)


def format_bytes(value: bytes) -> str:
    return " ".join(f"{byte:02X}" for byte in value)


def is_define_enabled(engine: Path, define: str) -> bool:
    config_path = engine / "include" / "config.h"
    if not config_path.is_file():
        return False

    pattern = re.compile(rf"^\s*#\s*define\s+{re.escape(define)}\b")
    for line in config_path.read_text(encoding="utf-8").splitlines():
        stripped = line.lstrip()
        if stripped.startswith("//"):
            continue
        if pattern.search(line):
            return True
    return False


def read_msgenc_text_entries(text_path: Path) -> list[str]:
    with text_path.open("r", encoding="utf-8", newline="") as file:
        text = file.read()

    # The C++ encoder reads through an MSYS text stream. Existing archives use
    # CRCRLF separators; MSYS text translation turns those into CRLF before the
    # encoder's custom CR/LF splitter runs.
    text = text.replace("\r\n", "\n")

    entries: list[str] = []
    pos = 0
    while True:
        text = text[pos:]
        if not text:
            break

        delimiters = [
            index for index in (text.find("\r"), text.find("\n")) if index != -1
        ]
        first_delimiter = min(delimiters) if delimiters else -1
        if first_delimiter == -1:
            entries.append(text)
            break

        entries.append(text[:first_delimiter])
        search_pos = min(first_delimiter + 1, len(text) - 1)
        next_pos = max(
            text.rfind("\r", 0, search_pos + 1),
            text.rfind("\n", 0, search_pos + 1),
        )
        if next_pos == -1:
            break
        pos = next_pos + 1

    return entries


def check_arm9(engine: Path) -> list[str]:
    arm9_path = engine / "base" / "arm9.bin"
    if not arm9_path.is_file():
        return [f"missing build output: {arm9_path}"]

    data = arm9_path.read_bytes()
    failures: list[str] = []
    expected_entries = list(ARM9_EXPECTED)
    if not is_define_enabled(engine, "IMPLEMENT_NEW_EV_IV_VIEWER"):
        expected_entries.extend(ARM9_EV_IV_CLEAN_IF_DISABLED)

    for address, expected_hex, label in expected_entries:
        expected = parse_bytes(expected_hex)
        offset = address - 0x02000000
        actual = data[offset : offset + len(expected)]
        if actual != expected:
            failures.append(
                f"arm9 {address:08X} {label}: got {format_bytes(actual)}, "
                f"expected {format_bytes(expected)}"
            )
    return failures


def check_config_sources(engine: Path) -> list[str]:
    failures: list[str] = []
    for define in sorted(DEFERRED_WILD_HOOK_CONFIGS):
        if is_define_enabled(engine, define):
            failures.append(
                f"config {define}: deferred wild encounter hook config must "
                "stay disabled for the stable Generations-aligned wild hook"
            )
    return failures


def check_overlays(engine: Path) -> list[str]:
    if is_define_enabled(engine, GENERATIONS_WILD_HOOK_CONFIG):
        return []

    y9_path = engine / "base" / "overarm9.bin"
    overlay_dir = engine / "base" / "overlay"
    if not y9_path.is_file():
        return [f"missing build output: {y9_path}"]

    y9 = y9_path.read_bytes()
    failures: list[str] = []
    for overlay_id, address, expected_hex, label in OVERLAY_EXPECTED:
        overlay_path = overlay_dir / f"overlay_{overlay_id:04}.bin"
        if not overlay_path.is_file():
            failures.append(f"missing build output: {overlay_path}")
            continue

        expected = parse_bytes(expected_hex)
        overlay_base = struct.unpack_from("<I", y9, overlay_id * 0x20 + 0x4)[0]
        offset = address - overlay_base
        actual = overlay_path.read_bytes()[offset : offset + len(expected)]
        if actual != expected:
            failures.append(
                f"overlay {overlay_id:04} {address:08X} {label}: "
                f"got {format_bytes(actual)}, expected {format_bytes(expected)}"
            )
    return failures


def check_text_sources(engine: Path) -> list[str]:
    failures: list[str] = []
    text_dir = engine / "data" / "text"
    for archive_id, expected_entries in TEXT_EXPECTED.items():
        text_path = text_dir / f"{archive_id}.txt"
        if not text_path.is_file():
            text_path = text_dir / f"{archive_id:03}.txt"
        if not text_path.is_file():
            failures.append(f"missing text source: {text_path}")
            continue

        entries = text_path.read_text(encoding="utf-8").splitlines()
        for entry_id, expected, label in expected_entries:
            if entry_id >= len(entries):
                failures.append(
                    f"text {archive_id} entry {entry_id} {label}: "
                    f"file has only {len(entries)} entries"
                )
                continue

            actual = entries[entry_id]
            if actual != expected:
                failures.append(
                    f"text {archive_id} entry {entry_id} {label}: "
                    f"got {actual!r}, expected {expected!r}"
                )

        compact_expected_entries = TEXT_COMPACT_EXPECTED.get(archive_id)
        if compact_expected_entries is None:
            continue

        compact_entries = read_msgenc_text_entries(text_path)
        for entry_id, expected, label in compact_expected_entries:
            if entry_id >= len(compact_entries):
                failures.append(
                    f"text {archive_id} compact entry {entry_id} {label}: "
                    f"file has only {len(compact_entries)} compact entries"
                )
                continue

            actual = compact_entries[entry_id]
            if actual != expected:
                failures.append(
                    f"text {archive_id} compact entry {entry_id} {label}: "
                    f"got {actual!r}, expected {expected!r}"
                )
    return failures


def check_script_sources(engine: Path) -> list[str]:
    failures: list[str] = []
    for script_relpath, expected_patterns in SCRIPT_EXPECTED.items():
        script_path = engine / script_relpath
        if not script_path.is_file():
            failures.append(f"missing script source: {script_path}")
            continue

        text = script_path.read_text(encoding="utf-8")
        for pattern, label in expected_patterns:
            if re.search(pattern, text, re.DOTALL) is None:
                failures.append(f"script {script_relpath} {label}: pattern not found")

    for script_relpath, text_bank_id in SCRIPT_TEXT_BANKS.items():
        script_path = engine / script_relpath
        text_path = engine / "data" / "text" / f"{text_bank_id:03}.txt"
        if not text_path.is_file():
            text_path = engine / "data" / "text" / f"{text_bank_id}.txt"
        if not script_path.is_file() or not text_path.is_file():
            continue

        script = script_path.read_text(encoding="utf-8")
        entries = text_path.read_text(encoding="utf-8").splitlines()
        for match in re.finditer(
            r"\b(?:npc_msg|non_npc_msg|simple_npc_msg)\s+(\d+)\b", script
        ):
            entry_id = int(match.group(1))
            line_number = script.count("\n", 0, match.start()) + 1
            if entry_id >= len(entries):
                failures.append(
                    f"script {script_relpath}:{line_number} text bank "
                    f"{text_bank_id} entry {entry_id}: out of range"
                )
            elif entries[entry_id] == "":
                failures.append(
                    f"script {script_relpath}:{line_number} text bank "
                    f"{text_bank_id} entry {entry_id}: blank message"
                )
    return failures


def main() -> int:
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")

    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--engine",
        default=ENGINE,
        type=Path,
        help="Path to hg-engine-main.",
    )
    args = parser.parse_args()

    engine = args.engine.resolve()
    failures = (
        check_config_sources(engine)
        + check_arm9(engine)
        + check_overlays(engine)
        + check_text_sources(engine)
        + check_script_sources(engine)
    )
    if failures:
        print("Phase 1 stable validation failed:")
        for failure in failures:
            print(f"- {failure}")
        return 1

    print("Phase 1 stable validation passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
