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

`release/Pokemon-JohtoReforged-v0.1.2-text-restore/`

- Patched ROM SHA-256:
  `6B475E12BC0DB3B4A05E4F7211F1CA37BE5C3113E8190258D2E9D7FF66DA12B8`
- Xdelta SHA-256:
  `6167B11280C0F669A369A4A25E61FF708971B21A98E4E883F4CB77457B6FF23F`
- Patch verification: xdelta rebuild from the clean ROM matched the packaged
  patched ROM hash.

## Validation

After each phase 1 build, run:

`python tools\johto_reforged\validate_phase1_stable_hooks.py`

This checks that deferred summary UI, nature stat, party menu, party item-use,
and wild post-processing hook sites match clean HeartGold bytes. It also checks
that fragile party menu and summary screen text IDs remain aligned to clean
HeartGold entries.
