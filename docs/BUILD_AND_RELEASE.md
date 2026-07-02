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

`release/Pokemon-JohtoReforged-v0.1.1-ui-rollback/`

- Patched ROM SHA-256:
  `900B2A7935592D46081583EA0F949774C3CE08018DAB660F6D3A14C8E62DF923`
- Xdelta SHA-256:
  `D97369F176C05D0D4137E7FE9EEFF55B4E9678929E2C9B97956AA100B52667E7`
- Patch verification: xdelta rebuild from the clean ROM matched the packaged
  patched ROM hash.

## Validation

After each phase 1 build, run:

`python tools\johto_reforged\validate_phase1_stable_hooks.py`

This checks that deferred summary UI, nature stat, party menu, party item-use,
and wild post-processing hook sites match clean HeartGold bytes.
