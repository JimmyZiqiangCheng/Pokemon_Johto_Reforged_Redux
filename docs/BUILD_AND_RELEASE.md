# Build And Release

## ROM Input

Use a legally obtained US Pokemon HeartGold ROM. Keep the clean ROM outside
this repository; for example:

`<romhack-workspace>\Pokemon - HeartGold Version (USA).nds`

Expected SHA-256:

`65F02A56842B75AA92D775D56D657A56FE3FA993550B04DC20704AB82D760105`

For HG-engine builds, copy that file to:

`hg-engine-main/rom.nds`

## Build Route

Run `make` from `hg-engine-main` using the MSYS2 toolchain. The HG-engine
output ROM is `hg-engine-main/test.nds`.

From PowerShell on this machine, the verified route is:

```powershell
$env:MSYSTEM = 'UCRT64'
$env:CHERE_INVOKING = '1'
$env:MSYS2_PATH_TYPE = 'inherit'
$env:DEVKITARM = '/ucrt64'
Push-Location .\hg-engine-main
& 'C:\msys64\usr\bin\bash.exe' -lc 'make'
Pop-Location
```

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

`release/Pokemon-JohtoReforged-v0.5.4-wild-ha-no-roamers-test/`

- Patched ROM SHA-256:
  `F57471410BD769C90FBB755673B0FA3AAB67105D39583E45BBE9809E2B34D5AE`
- Xdelta SHA-256:
  `D093F3DDD97F297FA322A090F8208E80604241ACBF9BAABA53130FF1CBD36931`
- Patch verification: xdelta rebuild from the clean ROM matched the packaged
  patched ROM hash.
- Current local test load for the active working tree. It includes Step 3 wild
  encounter tables, Step 4 trainer rosters/level curve, the Step 5 item/mart
  changes currently present in the worktree, the Phase 6 postgame work present
  in the local tree, the re-enabled EV/IV summary viewer, the
  Generations-aligned wild hook, and restored natural wild hidden-ability
  rolling.
- The wild availability audit confirmed 211 / 211 non-legendary Gen 1-4
  evolution-family components covered, with no missing base/pre-evolution
  species, approved later regional base-form placements covered 19 / 19, and
  0 Perfect Johto-style encounter validation errors.
- Random legendary replacement is disabled after the
  `v0.5.3-roamers-availability-test` crash report.

## Validation

After each phase 1 build, run:

`python tools\johto_reforged\validate_phase1_stable_hooks.py`

This checks that deferred nature stat, party menu, and party item-use hook
sites match clean HeartGold bytes, while allowing the explicitly re-enabled
EV/IV summary hook, Generations baseline wild hook, and natural wild
hidden-ability rolling. It also checks that the random legendary overlay stays
disabled, that fragile save screen, battle command, move PP, party menu, and
summary screen text IDs remain aligned to clean HeartGold entries, that the
EV/IV summary viewer uses appended archive 302 runtime IDs 195-212, and that
the common script uses appended bank 40 IDs for reusable Repels.

After Phase 5 item changes, also run:

`python tools\johto_reforged\validate_phase5_items.py`

This checks that `MART_EXPANSION` is enabled, badge-gated mart stock has the
expected 104 entries and gate tiers, Max Candy is defined at item 1058, stocked
item prices match the reference economy, and badge-stocked candy icons are not
placeholders.

After Phase 6 postgame changes, also run:

`python tools\johto_reforged\validate_phase6_postgame.py`

This checks the Saffron Fighting Dojo script/text import, Phase 8 caught flags,
Champion Circuit trainer records, dossier species, text coverage, and the
assembled Dojo script hash when the Perfect Johto reference build is available.
