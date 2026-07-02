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

`release/Pokemon-JohtoReforged-v0.1.0-initial-qol/`

- Patched ROM SHA-256:
  `FFA25BA576C465083A69AEE9B5C229A20BB8028D6C8A434745111F3F0404FC16`
- Xdelta SHA-256:
  `14F6F8C009AA104BA559F96F33CBF1A1D3F8F8B0CD6BBDC0A1FFC283BCCF9C61`
- Patch verification: xdelta rebuild from the clean ROM matched the packaged
  patched ROM hash.
