#!/usr/bin/env python3
"""Validate phase 1 UI/runtime rollback bytes after an HG-engine build."""

from __future__ import annotations

import argparse
import struct
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
ENGINE = ROOT / "hg-engine-main"


ARM9_EXPECTED = [
    (0x02088B60, "20 21 DC 6C 26 1C 0E 42", "summary EV/IV viewer site"),
    (0x0208D2C4, "78 21 03 23 FF F7 D8 FA", "summary entry hook site"),
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


def parse_bytes(value: str) -> bytes:
    return bytes.fromhex(value)


def format_bytes(value: bytes) -> str:
    return " ".join(f"{byte:02X}" for byte in value)


def check_arm9(engine: Path) -> list[str]:
    arm9_path = engine / "base" / "arm9.bin"
    if not arm9_path.is_file():
        return [f"missing build output: {arm9_path}"]

    data = arm9_path.read_bytes()
    failures: list[str] = []
    for address, expected_hex, label in ARM9_EXPECTED:
        expected = parse_bytes(expected_hex)
        offset = address - 0x02000000
        actual = data[offset : offset + len(expected)]
        if actual != expected:
            failures.append(
                f"arm9 {address:08X} {label}: got {format_bytes(actual)}, "
                f"expected {format_bytes(expected)}"
            )
    return failures


def check_overlays(engine: Path) -> list[str]:
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


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--engine",
        default=ENGINE,
        type=Path,
        help="Path to hg-engine-main.",
    )
    args = parser.parse_args()

    engine = args.engine.resolve()
    failures = check_arm9(engine) + check_overlays(engine)
    if failures:
        print("Phase 1 stable hook validation failed:")
        for failure in failures:
            print(f"- {failure}")
        return 1

    print("Phase 1 stable hook validation passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
