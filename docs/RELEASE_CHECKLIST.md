# Release Checklist

## Before Build

- Confirm phase scope in `FEATURES_AND_CHANGES.md`.
- Confirm deferred systems are documented in `docs/KNOWN_LIMITATIONS.md`.
- Confirm the clean ROM SHA-256 matches the expected value.
- Confirm `hg-engine-main/rom.nds` is present and ignored by Git.

## Build

- Run the HG-engine build from `hg-engine-main`.
- Confirm `hg-engine-main/test.nds` is produced.
- Run `python tools\johto_reforged\validate_phase1_stable_hooks.py` for phase 1
  releases, including party menu and summary screen text ID checks.
- Generate a versioned release folder under `release/`.
- Generate an xdelta patch from the clean ROM to the patched ROM.
- Generate `SHA256SUMS.txt`.
- Write release notes in `README.txt`.

## Must Not Commit

- Clean ROMs.
- Patched ROMs.
- Save files.
- Build outputs.
