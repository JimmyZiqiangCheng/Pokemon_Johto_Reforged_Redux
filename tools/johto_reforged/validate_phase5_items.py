from __future__ import annotations

import hashlib
import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
ENGINE = ROOT / "hg-engine-main"


EXPECTED_GATES = {
    "ITEM_POKE_BALL": 0,
    "ITEM_SUPER_POTION": 1,
    "ITEM_GREAT_BALL": 3,
    "ITEM_ABILITY_CAPSULE": 3,
    "ITEM_LONELY_MINT": 3,
    "ITEM_SERIOUS_MINT": 3,
    "ITEM_HP_UP": 4,
    "ITEM_FIRE_STONE": 4,
    "ITEM_LINKING_CORD": 4,
    "ITEM_ULTRA_BALL": 5,
    "ITEM_HEALTH_CANDY": 5,
    "ITEM_QUICK_CANDY": 5,
    "ITEM_MACHO_BRACE": 5,
    "ITEM_POWER_WEIGHT": 5,
    "ITEM_KINGS_ROCK": 5,
    "ITEM_PRISM_SCALE": 5,
    "ITEM_ABILITY_PATCH": 6,
    "ITEM_PROTECTOR": 6,
    "ITEM_BLACK_AUGURITE": 6,
    "ITEM_GALARICA_WREATH": 6,
    "ITEM_FULL_RESTORE": 8,
    "ITEM_MAX_CANDY": 12,
}

EXPECTED_PRICES = {
    "ITEM_MAX_CANDY": 8000,
    "ITEM_HEALTH_CANDY": 2000,
    "ITEM_MIGHTY_CANDY": 2000,
    "ITEM_TOUGH_CANDY": 2000,
    "ITEM_SMART_CANDY": 2000,
    "ITEM_COURAGE_CANDY": 2000,
    "ITEM_QUICK_CANDY": 2000,
    "ITEM_ABILITY_CAPSULE": 1000,
    "ITEM_ABILITY_PATCH": 1000,
    "ITEM_LONELY_MINT": 1000,
    "ITEM_SERIOUS_MINT": 1000,
    "ITEM_HP_UP": 3000,
    "ITEM_PROTEIN": 3000,
    "ITEM_POWER_WEIGHT": 3000,
    "ITEM_POWER_ANKLET": 3000,
    "ITEM_POMEG_BERRY": 200,
    "ITEM_TAMATO_BERRY": 200,
    "ITEM_FIRE_STONE": 2500,
    "ITEM_LINKING_CORD": 2500,
    "ITEM_KINGS_ROCK": 2500,
    "ITEM_PROTECTOR": 2500,
    "ITEM_BLACK_AUGURITE": 2500,
    "ITEM_PEAT_BLOCK": 2500,
}

IV_CANDIES = [
    "ITEM_HEALTH_CANDY",
    "ITEM_MIGHTY_CANDY",
    "ITEM_TOUGH_CANDY",
    "ITEM_SMART_CANDY",
    "ITEM_COURAGE_CANDY",
    "ITEM_QUICK_CANDY",
]

ICON_NAMES = {
    "ITEM_HEALTH_CANDY": "health_candy.png",
    "ITEM_MIGHTY_CANDY": "mighty_candy.png",
    "ITEM_TOUGH_CANDY": "tough_candy.png",
    "ITEM_SMART_CANDY": "smart_candy.png",
    "ITEM_COURAGE_CANDY": "courage_candy.png",
    "ITEM_QUICK_CANDY": "quick_candy.png",
    "ITEM_MAX_CANDY": "max_candy.png",
}


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="replace")


def parse_defines(path: Path) -> dict[str, int]:
    values: dict[str, int] = {}
    for line in read_text(path).splitlines():
        match = re.match(r"#define\s+(ITEM_[A-Z0-9_]+)\s+(\d+)", line)
        if match:
            values[match.group(1)] = int(match.group(2))
    return values


def parse_equ(path: Path) -> dict[str, int]:
    values: dict[str, int] = {}
    for line in read_text(path).splitlines():
        match = re.match(r"\.equ\s+(ITEM_[A-Z0-9_]+),\s+(\d+)", line)
        if match:
            values[match.group(1)] = int(match.group(2))
    return values


def parse_badge_mart() -> dict[str, int]:
    text = read_text(ENGINE / "src" / "field" / "mart.c")
    match = re.search(r"const struct BadgeMartItems sBadgeMart\[\]\s*=\s*\{(.*?)\n\};", text, re.S)
    if not match:
        raise AssertionError("sBadgeMart table not found")
    return {
        item: int(badges)
        for item, badges in re.findall(r"\{\s*(ITEM_[A-Z0-9_]+)\s*,\s*(\d+)\s*\}", match.group(1))
    }


def item_block(item: str) -> str:
    text = read_text(ENGINE / "data" / "itemdata" / "itemdata.c")
    match = re.search(r"\[" + re.escape(item) + r"\]\s*=\s*\{(.*?)\n\},", text, re.S)
    if not match:
        raise AssertionError(f"{item} itemdata block not found")
    return match.group(1)


def item_price(item: str) -> int:
    match = re.search(r"ITEM_PRICE\((\d+)\)", item_block(item))
    if not match:
        raise AssertionError(f"{item} price not found")
    return int(match.group(1))


def item_attr(item: str, attr: str) -> str:
    match = re.search(r"\." + attr + r"\s*=\s*([^,\n]+)", item_block(item))
    if not match:
        raise AssertionError(f"{item}.{attr} not found")
    return match.group(1).strip()


def file_hash(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def validate() -> list[str]:
    errors: list[str] = []

    config = read_text(ENGINE / "include" / "config.h")
    if not re.search(r"^\s*#define\s+MART_EXPANSION\b", config, re.M):
        errors.append("MART_EXPANSION is not enabled")

    c_items = parse_defines(ENGINE / "include" / "constants" / "item.h")
    asm_items = parse_equ(ENGINE / "asm" / "include" / "items.inc")
    if c_items.get("ITEM_MAX_CANDY") != 1058:
        errors.append("ITEM_MAX_CANDY is missing or not 1058 in C constants")
    if asm_items.get("ITEM_MAX_CANDY") != 1058:
        errors.append("ITEM_MAX_CANDY is missing or not 1058 in asm constants")

    mart = parse_badge_mart()
    if len(mart) != 104:
        errors.append(f"badge mart has {len(mart)} entries, expected 104")
    if len(mart) > 203:
        errors.append(f"badge mart has {len(mart)} entries, over UI limit 203")

    for item, badges in EXPECTED_GATES.items():
        if mart.get(item) != badges:
            errors.append(f"{item} gate is {mart.get(item)}, expected {badges}")

    forbidden = [item for item in mart if any(token in item for token in ["Z_", "DYNAMAX", "GIGANTAMAX", "TERA", "MEGA", "PRIMAL"])]
    if forbidden:
        errors.append("forbidden gimmick items stocked: " + ", ".join(sorted(forbidden)))

    for item, price in EXPECTED_PRICES.items():
        actual = item_price(item)
        if actual != price:
            errors.append(f"{item} price is {actual}, expected {price}")

    for item in [*IV_CANDIES, "ITEM_MAX_CANDY"]:
        for attr, expected in {
            "fieldPocket": "POCKET_MEDICINE",
            "fieldUseFunc": "33",
            "partyUse": "1",
        }.items():
            actual = item_attr(item, attr)
            if actual != expected:
                errors.append(f"{item}.{attr} is {actual}, expected {expected}")

    names = read_text(ENGINE / "data" / "text" / "222.txt").splitlines()
    if len(names) <= 1058 or names[1058] != "Max Candy":
        errors.append("text/222 item name for ITEM_MAX_CANDY is not Max Candy")

    placeholder = ENGINE / "data" / "graphics" / "item" / "unknown_7a.png"
    placeholder_hash = file_hash(placeholder)
    for item, filename in ICON_NAMES.items():
        icon = ENGINE / "data" / "graphics" / "item" / filename
        if not icon.exists():
            errors.append(f"{item} icon missing: {icon}")
        elif file_hash(icon) == placeholder_hash:
            errors.append(f"{item} icon still matches placeholder unknown_7a.png")

    itemgra = read_text(ENGINE / "data" / "graphics" / "itemgra.mk")
    if "max_candy.png" not in itemgra:
        errors.append("itemgra.mk does not reference max_candy.png")

    return errors


def main() -> int:
    errors = validate()
    if errors:
        print("Phase 5 item validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1

    print("Phase 5 item validation passed: badge mart gates, prices, Max Candy, and stocked icons are valid.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
