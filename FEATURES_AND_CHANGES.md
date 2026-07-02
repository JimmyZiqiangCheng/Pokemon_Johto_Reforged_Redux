# Pokemon Johto Reforged - Features and Changes

Document version: v2026.07.02-qol-text-remap
Last updated: 2026-07-02

This project restarts Pokemon Johto Reforged from a smaller, safer baseline.
The abandoned `perfect_johto` project remains the design reference, but changes
will be reintroduced one phase at a time with a build and release at each step.

## Design Philosophy

- Build a polished HeartGold/HG-engine Johto experience without trying to land
  every feature in one pass.
- Keep each phase independently buildable and playtestable.
- Prefer conservative runtime stability over feature count.
- Document all phase scope, deferred work, known risks, release files, and ROM
  hashes.
- Do not commit or redistribute copyrighted ROM data.

## Phase Plan

| Phase | Scope | Status |
| --- | --- | --- |
| 1 | Initial HG-engine build with important low-risk QOL toggles only | Complete in `v0.1.5-qol-text-remap` |
| 2 | Pokemon stats, ability, move, and typing changes | Planned |
| 3 | Wild encounter table changes | Planned |
| 4 | Trainer updates | Planned |
| 5 | Item changes | Planned |
| 6 | Postgame feature expansion | Planned |

## Phase 1 QOL Baseline

Enabled:

- Fast text.
- Reusable TMs.
- Deletable HMs.
- Capture EXP.
- Critical captures.
- Hidden Abilities support.
- Reusable Repels.
- Vitamin EV cap update.
- Disabled overworld poison damage.
- Anti-piracy patching.

Deferred from phase 1:

- Save expansion, expanded PC boxes, and expanded item pockets.
- Mega Evolution and Primal Reversion.
- EV/IV summary viewer and nature stat UI.
- Mint/nature stat override hooks.
- Party item-use overrides for custom candies, mints, Ability Capsule, and
  Ability Patch.
- Wild Pokemon post-processing hooks for natural hidden ability/form rewrites.
- HG-engine-added save/general text messages that shift vanilla save UI IDs.
- HG-engine-added battle text messages that shift vanilla battle UI IDs.
- Mart/economy changes.
- Running Shoes script changes, AutoRun, fast Surf, and field moves without
  teaching HMs.

## Key Docs

- `docs/README.md`
- `docs/PROJECT_PHASES.md`
- `docs/QOL_FEATURES.md`
- `docs/BUILD_AND_RELEASE.md`
- `docs/PLAYTEST_CHECKLIST.md`
- `docs/RELEASE_CHECKLIST.md`
- `docs/KNOWN_LIMITATIONS.md`

## Current Release

- Version: `v0.1.5-qol-text-remap`
- Folder: `release/Pokemon-JohtoReforged-v0.1.5-qol-text-remap/`
- Clean ROM SHA-256:
  `65F02A56842B75AA92D775D56D657A56FE3FA993550B04DC20704AB82D760105`
- Patched ROM SHA-256:
  `858041E9BB724FAC145B82C19E5312080982598CCAF22EA4F99DD55F10D18D84`
- Xdelta SHA-256:
  `96246EB08FB57CFDA6FCBC8DA3E8483035EC1966A85282F0470AADA5DFAB5A63`

## Release History

| Version | Notes |
| --- | --- |
| `v0.1.5-qol-text-remap` | Supersedes `v0.1.4`; reintroduces reusable Repel prompt text by appending clean bank 40 entries at IDs 234 and 236, then remapping the common script to those appended IDs. Keeps save, battle, party, and summary UI text IDs stable. |
| `v0.1.4-save-text-restore` | Supersedes `v0.1.3`; restores clean HeartGold save/general text archive IDs after HG-engine text changes shifted bank 40, causing the save prompt to display the Hall of Fame corruption warning. Adds validation for those IDs. |
| `v0.1.3-battle-text-restore` | Supersedes `v0.1.2`; restores clean HeartGold battle text archive IDs for battle command, move PP, and Safari labels after HG-engine text changes shifted bank 197. Adds validation for those IDs. |
| `v0.1.2-text-restore` | Supersedes `v0.1.1`; restores clean HeartGold text archive IDs for party menu and summary screen labels after HG-engine-added text shifted entries 300 and 302. Adds validation for those fragile IDs. |
| `v0.1.1-ui-rollback` | Supersedes `v0.1.0`; restores clean HeartGold bytes for deferred summary UI, nature stat, party context, party item-use, and wild post-processing hook sites after party/summary text corruption was reported. |
| `v0.1.0-initial-qol` | Initial HG-engine QOL baseline; superseded because some deferred support patches still affected summary and party UI code paths. |
