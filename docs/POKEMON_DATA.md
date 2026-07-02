# Pokemon Data Changes

This is the reference entry point for Phase 2 Pokemon-specific data changes:
base stats, abilities, typings, learnsets, moves, baby species mappings, and
evolution access. The active data is imported from the abandoned
`<romhack-workspace>\perfect_johto` reference project, limited to the
Pokemon-data surfaces covered by Phase 2.

## Quick Reference

| Topic | Primary reference |
| --- | --- |
| Scope and allowed species/forms | `docs/PROJECT_SCOPE.md`, `docs/APPROVED_LATER_EXCEPTIONS.md` |
| Base stats, ability slots, and Luminescent source pass | `docs/LUMINESCENT_DATA_REFRESH.md` |
| Type modernization and STAB support | `docs/TYPE_AND_LEARNSET_CHANGES.md` |
| Egg move and late-level learnset rules | `docs/LEARNSET_ACCESSIBILITY.md` |
| Evolution method changes | `docs/EVOLUTIONS.md` |
| Phase boundaries | `docs/PROJECT_PHASES.md` |

## Source Files

- Species personal data: `hg-engine-main/data/Species.c`.
- Hidden ability data: `hg-engine-main/data/HiddenAbilityTable.c`.
- Baby species mapping: `hg-engine-main/data/BabyMons.c`.
- Level-up, egg, machine, and tutor learnset source:
  `hg-engine-main/data/learnsets/learnsets.json`.
- Learnset build helper: `hg-engine-main/scripts/build_learnsets.py`.
- Evolution data: `hg-engine-main/data/Evolutions.c`.
- Move data: `hg-engine-main/data/Moves.c`; this already matched the Perfect
  Johto reference exactly before the Phase 2 import.

## Scope Rules

- All Generation 1-4 Pokemon are in scope.
- Later-generation direct evolutions, regional forms, and new forms are allowed only when they belong to Generation 1-4 families and are listed in `docs/APPROVED_LATER_EXCEPTIONS.md`.
- Unrelated Generation 5+ Pokemon, unrelated later forms, Mega Evolution, Primal Reversion, Z-Moves, Dynamax/Gigantamax, Terastalization, and similar battle gimmicks remain out of scope.
- The engine still contains later-generation species, moves, abilities, items,
  and mechanics as internal capacity. Gameplay exposure is restricted by the
  phase plan; encounters, trainers, and marts are now imported through Phases 3,
  4, and 5, while scripts and postgame access remain later phases.

## Stats And Abilities

- Generation 1-4 base species rows and relevant native Generation 3-4 form rows were refreshed against Luminescent Platinum 3.0 as the primary data standard.
- The Luminescent pass covers base stats and ability slots for the target species/form set. Renegade Platinum and Polished Crystal remain secondary design references, not overrides.
- Ability modernization is allowed when it supports Pokemon identity, role variety, and Johto replayability.
- Hidden ability slots remain in the data. Ordinary wild Pokemon can roll their
  hidden ability as another natural ability slot through
  `NATURAL_WILD_HIDDEN_ABILITIES`; broader wild post-processing remains
  deferred.
- Ability Capsule and Ability Patch are stocked through the Phase 5 badge mart;
  their custom party-use behavior remains guarded by
  `IMPLEMENT_PARTY_ITEM_USE_OVERRIDES`.
- Custom defensive ability behavior, Immortal Shell, and one-off personalized pseudo-legendary ability changes remain out of scope.

## Typing

Typing modernization is restrained and species-identity driven. The complete type-change list and STAB support audit live in `docs/TYPE_AND_LEARNSET_CHANGES.md`.

Important constraints:

- No type chart change has been made.
- Rock no longer being weak to Ground remains out of scope.
- Type changes do not by themselves change base stats, evolution methods, encounter scope, catch rates, EV yields, held items, or growth data.
- Project-added secondary types are audited for reasonable level-up attacking move access.

## Moves And Learnsets

- Move battle behavior and move data are not a project feature area right now; no custom move-behavior pass is documented.
- Level-up learnsets preserve local extras and append missing Luminescent Platinum 3.0 level-up moves at their Luminescent levels.
- Luminescent move IDs are resolved through Luminescent move names before being mapped to local `MOVE_*` constants, because post-Gen 4 numeric IDs do not fully match this engine.
- Egg moves are also level-up accessible for every Pokemon with egg moves.
- Non-legendary level-up moves are compressed below level 60. Legendary, mythical, Ultra Beast, and comparable one-off Pokemon keep late signature pacing.
- Evolved forms inherit earlier-form level-up moves more consistently.

## Evolutions

Evolution changes are documented in `docs/EVOLUTIONS.md`.

The major rules are:

- Approved-scope trade-only evolutions are replaced with item-use or other non-trade methods where appropriate.
- Trade-with-item evolutions use direct item-use methods.
- Known-move evolutions are used for Wyrdeer, Annihilape, and Sirfetch'd.
- Dudunsparce Three-Segment and Ursaluna Bloodmoon have simple level-up access through their standard final forms.
- Required evolution-item access is provided by the Phase 5 badge-gated mart.

## Validation

Validate the imported data with JSON parsing, learnset generation, source hash
checks against the Perfect Johto reference, and the existing stable-hook guard:

```powershell
python -c "import json; json.load(open(r'hg-engine-main/data/learnsets/learnsets.json', encoding='utf-8'))"
Push-Location hg-engine-main
python scripts/build_learnsets.py --learnsets data/learnsets/learnsets.json --machineout <temp>/MachineMoveLearnsets.c --levelupout <temp>/LevelupLearnsets.c --eggout <temp>/EggLearnsets.c --tutorout <temp>/TutorMoveLearnsets.c
Pop-Location
python tools/johto_reforged/validate_phase1_stable_hooks.py
```

The phase-1 stable-hook validator is still required after a build because this
phase intentionally leaves unstable UI, party item-use, and wild post-processing
hooks deferred.
