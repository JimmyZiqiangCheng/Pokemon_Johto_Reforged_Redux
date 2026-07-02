# Pokemon Johto Reforged Documentation

Use `FEATURES_AND_CHANGES.md` at the project root as the feature index. This
folder tracks implementation scope, phase boundaries, release process, and
playtest notes.

## Start Here

- `PROJECT_PHASES.md`: the six-phase rollout and what belongs in each phase.
- `QOL_FEATURES.md`: phase 1 enabled and deferred QOL toggles.
- `POKEMON_DATA.md`: phase 2 Pokemon data sources, scope, and validation.
- `TYPE_AND_LEARNSET_CHANGES.md`: imported type modernization and learnset
  rules.
- `EVOLUTIONS.md`: imported no-trade and special-form evolution rules.
- `ENCOUNTER_SYSTEMS.md`: Step 3 encounter-system entry point.
- `WILD_ENCOUNTERS.md`: imported wild encounter table rules and sources.
- `RARE_ENCOUNTERS.md`: rare-find slot rules and placement rules.
- `RANDOM_LEGENDARY_SYSTEM.md`: disabled random roaming legendary source
  design, badge gates, and rates.
- `TRAINER_TEAMS.md`: Step 4 trainer-team import, level curve, and validation.
- `BOSS_BATTLES.md`: Step 4 boss roster and level-band summary.
- `ITEMS_AND_MARTS.md`: Step 5 badge-gated mart stock, economy, and item
  behavior notes.
- `KANTO_POSTGAME.md`: Phase 6 Saffron Fighting Dojo postgame hub.
- `CHAMPION_CIRCUIT.md`: Phase 6 repeatable late-postgame Champion Circuit.
- `LEGENDARIES.md`: Phase 6 proper Gen 1-4 legendary and mythical access.
- `REFERENCE_REPOS.md`: local and upstream reference repos, including HeartGold
  Generations 2.0.
- `BUILD_AND_RELEASE.md`: local ROM input, build route, release layout, and
  hash expectations.
- `PLAYTEST_CHECKLIST.md`: manual smoke tests before a phase is considered
  stable.
- `RELEASE_CHECKLIST.md`: release steps and required artifacts.
- `KNOWN_LIMITATIONS.md`: deliberately deferred systems and current risks.

## Source Reference

The abandoned project at `<romhack-workspace>\perfect_johto` is the design
reference. Reintroduce features only through the phase plan and
verify each release; Phase 2 imports only Pokemon data surfaces from that
reference. Phase 3 imports encounter table surfaces and the scoped random
roaming legendary overlay from that reference. Phase 4 imports the trainer
table and level-curve pass from that reference. Phase 5 imports the badge mart,
item economy, and customization item data from that reference. Phase 6 imports
the Saffron Fighting Dojo postgame hub, Champion Circuit, and scripted
legendary/mythical dossier access from that reference.

HeartGold Generations 2.0 is available as an HG-engine QOL reference at
`<romhack-workspace>\reference_repos\heartgold_generations_hg_engine_2_0`.
See `REFERENCE_REPOS.md` before porting from it.
