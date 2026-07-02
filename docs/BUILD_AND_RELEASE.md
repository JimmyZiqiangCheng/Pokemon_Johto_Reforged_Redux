# Build And Release

## ROM Input

Use a legally obtained US Pokemon HeartGold ROM. The requested filename was:

`C:\Users\jimmy\Documents\pokemon_romhacks\4787 - Pokemon - HeartGold Version (USA).nds`

On this machine the matching clean ROM currently resolves as:

`C:\Users\jimmy\Documents\pokemon_romhacks\Pokemon  HeartGold Version.nds`

Expected SHA-256:

`65F02A56842B75AA92D775D56D657A56FE3FA993550B04DC20704AB82D760105`

For HG-engine builds, copy that file to:

`hg-engine-main/rom.nds`

## Build Route

Run `make` from `hg-engine-main` using the MSYS2 toolchain. The HG-engine
output ROM is `hg-engine-main/test.nds`.

## Release Layout

Versioned releases live under:

`release/Pokemon-JohtoReforged-vX.Y.Z-label/`

Each release should include:

- The `.xdelta` patch.
- The locally generated patched `.nds` ROM.
- `README.txt`.
- `SHA256SUMS.txt`.

Do not commit or redistribute `.nds` files. They are local convenience outputs
only.

## Current Release

`release/Pokemon-JohtoReforged-v0.1.3-battle-text-restore/`

- Patched ROM SHA-256:
  `A05713B4B96B8DD072F787DE899168A7AA7B99ED03C2E8F5B3C3904674645B82`
- Xdelta SHA-256:
  `B26A68ABACEC41AFED9E9DF0C4CE1CBD60C3F2D7FFB58338CC73D1CD9A6F0BFB`
- Patch verification: xdelta rebuild from the clean ROM matched the packaged
  patched ROM hash.

## Validation

After each phase 1 build, run:

`python tools\johto_reforged\validate_phase1_stable_hooks.py`

This checks that deferred summary UI, nature stat, party menu, party item-use,
and wild post-processing hook sites match clean HeartGold bytes. It also checks
that fragile battle command, move PP, party menu, and summary screen text IDs
remain aligned to clean HeartGold entries.
