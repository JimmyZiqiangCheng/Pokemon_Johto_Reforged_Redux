# Pokemon Johto Reforged - Features and Changes

Document version: v2026.07.02-wild-ha-no-roamers
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
| 2 | Pokemon stats, ability, move, typing, evolution, and learnset changes | Packaged in `v0.2.0-phase2-wild-ha-hoothoot-test` |
| 3 | Wild encounter table changes | Implemented in working tree; runtime testing pending |
| 4 | Trainer updates | Implemented in working tree; runtime testing pending |
| 5 | Item changes | Implemented in working tree; local build passed; runtime testing pending |
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
- EV/IV summary viewer with appended summary archive 302 runtime labels at IDs
  195-212, avoiding the text-bank shifts that broke summary labels before.

Deferred from phase 1:

- Save expansion, expanded PC boxes, and expanded item pockets.
- Mega Evolution and Primal Reversion.
- Mint/nature stat override hooks.
- Party item-use overrides for custom candies, mints, Ability Capsule, and
  Ability Patch.
- Broad wild Pokemon post-processing hooks for form rewrites.
- HG-engine-added save/general text messages that shift vanilla save UI IDs.
- HG-engine-added battle text messages that shift vanilla battle UI IDs.
- Mart/economy changes.
- Running Shoes script changes, AutoRun, fast Surf, and field moves without
  teaching HMs.

## Phase 2 Pokemon Data

Imported from the abandoned `perfect_johto` reference, limited to Pokemon data:

- `hg-engine-main/data/Species.c`: Perfect Johto species personal data,
  including base stats, types, normal ability slots, and related species fields.
- `hg-engine-main/data/HiddenAbilityTable.c`: Perfect Johto hidden ability
  slots.
- `hg-engine-main/data/Evolutions.c`: Perfect Johto no-trade, item-use,
  known-move, and special-form evolution data.
- `hg-engine-main/data/BabyMons.c`: Perfect Johto baby species mappings for
  phase-2 special forms.
- `hg-engine-main/data/learnsets/learnsets.json`: Perfect Johto active level-up,
  egg, machine, and tutor learnset source.
- `hg-engine-main/data/Moves.c` already matched Perfect Johto exactly before
  this phase.
- Hidden ability slots remain in data. Ordinary natural wild hidden-ability
  rolling is restored through the Generations-aligned wild hook, treating hidden
  abilities as another natural ability slot during wild Pokemon generation.

Phase 2 kept later phase boundaries intact: trainer rosters, mart/item access,
postgame scripts, and unstable party item-use hooks were deferred to later
phases.

## Phase 3 Wild Encounters

Imported from the abandoned `perfect_johto` reference:

- `hg-engine-main/data/Encounters.c`: main wild encounter table update,
  including regular encounter pools and rare-find slot placements.
- `hg-engine-main/data/SafariEncounters.c`: Safari encounter table update.
- `hg-engine-main/data/Headbutt.c` already matched the Perfect Johto reference.
- `hg-engine-main/src/field/encounter_check.c`: fishing slot 4 changed to a
  4% low-rate slot for rare-find/filler consistency.
- `hg-engine-main/src/field/enemy_party.c`: the baseline HG-engine/Generations
  wild hook is active for held items, passive forms, Unown forms, scripted
  hidden abilities, and natural wild hidden-ability rolling.
- `hg-engine-main/src/field/enemy_party.c`: badge-gated random roaming
  legendary overlay source remains in the tree but is compiled out after the
  `v0.5.3-roamers-availability-test` crash report.
- The final wild availability audit confirms all non-legendary Gen 1-4
  evolution-family components are represented in wild sources, with no missing
  base/pre-evolution species.

## Phase 4 Trainers

Imported from the abandoned `perfect_johto` reference:

- `hg-engine-main/data/Trainers.c`: full trainer-team, boss-team, rematch, and
  level-curve update.
- Gym Leaders, Elite Four, Champions, Red, major rivals, Rocket leaders, and
  other major bosses use six-Pokemon teams where required by the reference.
- Johto leader first-clear curve runs from Falkner 13-14 through Clair 46-50.
- First Elite Four and Champion curve runs from Will 50-54 through Lance 58-60.
- Kanto leaders rise through Blue 78-82, with rematches and late-postgame
  records extending higher.
- Regular trainers receive controlled level scaling and thematic Gen 3-4
  variety replacements without broad party-size inflation.

## Phase 5 Items

Imported from the abandoned `perfect_johto` reference:

- `hg-engine-main/src/field/mart.c`: standard marts now use the 104-entry
  badge-gated stock table.
- `hg-engine-main/include/config.h`: `MART_EXPANSION` is enabled so normal mart
  purchases route through badge-count stock generation.
- `hg-engine-main/data/itemdata/itemdata.c`: item prices and field-use metadata
  match the Perfect Johto item economy for stocked customization, training, and
  evolution items.
- `ITEM_MAX_CANDY` is defined at item ID 1058 in C and asm constants, with
  item data, name text, and item graphics.
- `hg-engine-main/src/individual/PartyMenu_HandleUseItemOnMon.c`: IV candy and
  Max Candy source behavior is imported, while the broader party item-use hook
  remains config-gated for runtime stability.

Badge-gated item access:

- 0-2 badges: core balls, medicine, status heals, Escape Rope, and Repels.
- 3 badges: EV feathers, EV-reduction berries, mints, and Ability Capsule.
- 4 badges: EV vitamins, common stones, Oval Stone, and Linking Cord.
- 5 badges: IV stat candies, Macho Brace, Power items, and trade-item
  replacements.
- 6 badges: Ability Patch and broader evolution item access.
- 12 badges: Max Candy.

## Phase 6 Postgame

Imported from the abandoned `perfect_johto` Phase 8 reference:

- `hg-engine-main/armips/scr_seq/scr_seq_00832_phase8_dojo.s`: Saffron
  Fighting Dojo postgame hub, existing visible Gym Leader rematch scripts,
  Champion Circuit menu, and scripted legendary/mythical dossier battles.
- `hg-engine-main/data/text/533.txt`: Dojo hub, rematch, Champion Circuit, and
  dossier menu text.
- `hg-engine-main/armips/include/flags.s`: named Phase 8 caught-flag aliases
  for Dojo-only dossier captures.
- Champion Circuit repeatable battles: Lance, Blue, Red, Steven, Wallace, and
  Cynthia.
- Proper Gen 1-4 legendary/mythical access: native Raikou/Entei roamers plus
  Dojo dossier battles for the remaining covered species.

The random legendary wild overlay is disabled after the
`v0.5.3-roamers-availability-test` crash report; the Dojo dossier battles
remain the deterministic proper-access path for legendary and mythical captures.

## Key Docs

- `docs/README.md`
- `docs/PROJECT_PHASES.md`
- `docs/QOL_FEATURES.md`
- `docs/POKEMON_DATA.md`
- `docs/TYPE_AND_LEARNSET_CHANGES.md`
- `docs/LEARNSET_ACCESSIBILITY.md`
- `docs/EVOLUTIONS.md`
- `docs/ENCOUNTER_SYSTEMS.md`
- `docs/WILD_ENCOUNTERS.md`
- `docs/RARE_ENCOUNTERS.md`
- `docs/RANDOM_LEGENDARY_SYSTEM.md`
- `docs/TRAINER_TEAMS.md`
- `docs/BOSS_BATTLES.md`
- `docs/ITEMS_AND_MARTS.md`
- `docs/KANTO_POSTGAME.md`
- `docs/CHAMPION_CIRCUIT.md`
- `docs/LEGENDARIES.md`
- `docs/LUMINESCENT_DATA_REFRESH.md`
- `docs/REFERENCE_REPOS.md`
- `docs/BUILD_AND_RELEASE.md`
- `docs/PLAYTEST_CHECKLIST.md`
- `docs/RELEASE_CHECKLIST.md`
- `docs/KNOWN_LIMITATIONS.md`

## Current Release

- Version: `v0.5.4-wild-ha-no-roamers-test`
- Folder: `release/Pokemon-JohtoReforged-v0.5.4-wild-ha-no-roamers-test/`
- Clean ROM SHA-256:
  `65F02A56842B75AA92D775D56D657A56FE3FA993550B04DC20704AB82D760105`
- Patched ROM SHA-256:
  `F57471410BD769C90FBB755673B0FA3AAB67105D39583E45BBE9809E2B34D5AE`
- Xdelta SHA-256:
  `D093F3DDD97F297FA322A090F8208E80604241ACBF9BAABA53130FF1CBD36931`

## Release History

| Version | Notes |
| --- | --- |
| `v0.5.4-wild-ha-no-roamers-test` | Supersedes `v0.5.3`; disables the random legendary overlay after the roamer crash report and restores natural wild hidden-ability rolling so hidden abilities are treated as another normal wild ability slot. |
| `v0.5.3-roamers-availability-test` | Supersedes `v0.5.2`; restores the badge-gated random legendary overlay at 1/4000 weaker/mystery tier and 1/8000 cover-worthy tier aggregate rates, keeps natural wild hidden-ability rolling disabled, and packages the final wild availability audit with no missing non-legendary base/pre-evolution species or approved regional base-form gaps. |
| `v0.5.2-wild-hook-fix` | Supersedes `v0.5.1`; keeps the EV/IV viewer fix but disables natural wild hidden-ability rolling and random roaming legendary replacement after wild encounter startup crashes, restoring the active wild hook to the HeartGold Generations baseline behavior. |
| `v0.5.1-ev-iv-viewer-test` | Supersedes `v0.5.0`; re-enables the EV/IV summary viewer using appended summary archive 302 runtime labels at IDs 195-212 while preserving vanilla summary labels at IDs 109-152. |
| `v0.5.0-current-encounters-trainers-items-test` | Packages Perfect Johto wild encounter tables, Safari tables, random roaming legendary encounter logic, Perfect Johto trainer rosters/level curve, and the active Phase 5 item/mart changes then present in the worktree. |
| `v0.2.0-phase2-wild-ha-hoothoot-test` | Packages Phase 2 Pokemon data from Perfect Johto, enables natural wild hidden ability rolling, installs the wild encounter hook needed for that code path, restores Route 29 after the temporary Hoothoot test, removes the forced-Hoothoot override, and adds the Intimidate ability popup plus missing popup text before the Attack drop. |
| `v0.1.5-qol-text-remap` | Supersedes `v0.1.4`; reintroduces reusable Repel prompt text by appending clean bank 40 entries at IDs 234 and 236, then remapping the common script to those appended IDs. Keeps save, battle, party, and summary UI text IDs stable. |
| `v0.1.4-save-text-restore` | Supersedes `v0.1.3`; restores clean HeartGold save/general text archive IDs after HG-engine text changes shifted bank 40, causing the save prompt to display the Hall of Fame corruption warning. Adds validation for those IDs. |
| `v0.1.3-battle-text-restore` | Supersedes `v0.1.2`; restores clean HeartGold battle text archive IDs for battle command, move PP, and Safari labels after HG-engine text changes shifted bank 197. Adds validation for those IDs. |
| `v0.1.2-text-restore` | Supersedes `v0.1.1`; restores clean HeartGold text archive IDs for party menu and summary screen labels after HG-engine-added text shifted entries 300 and 302. Adds validation for those fragile IDs. |
| `v0.1.1-ui-rollback` | Supersedes `v0.1.0`; restores clean HeartGold bytes for deferred summary UI, nature stat, party context, party item-use, and wild post-processing hook sites after party/summary text corruption was reported. |
| `v0.1.0-initial-qol` | Initial HG-engine QOL baseline; superseded because some deferred support patches still affected summary and party UI code paths. |
