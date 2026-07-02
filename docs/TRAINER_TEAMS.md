# Trainer Teams

Step 4 imports trainer teams from the abandoned Perfect Johto reference.

## Source

- Current source: `hg-engine-main/data/Trainers.c`.
- Reference source:
  `<romhack-workspace>\perfect_johto\hg-engine-main\hg-engine-main\data\Trainers.c`.
- Reference docs:
  `<romhack-workspace>\perfect_johto\docs\TRAINER_TEAMS.md`
  and
  `<romhack-workspace>\perfect_johto\docs\phase7_trainer_report.md`.
- Imported source SHA-256:
  `FC623FDFA8B91D6F2985294229785DB100B0C5A9EEDB778DD3BC372EF788E746`.

## Change Summary

- Gym Leaders, Elite Four, Champions, Red, and other major bosses use full
  six-Pokemon teams.
- Johto leader first-clear curve now runs from Falkner 13-14 through Clair
  46-50.
- First Elite Four and Champion curve runs from Will 50-54 through Lance 58-60.
- Kanto leaders are raised into the post-League curve, ending with Blue 78-82.
- Gym Leader rematches, Elite Four rematches, Lance rematches, Red, and
  Champion Circuit trainer records are raised for late-postgame play.
- Major Silver, Team Rocket Executive, and Giovanni/Rocket Boss records are
  expanded where their story role and level band support it.
- Regular trainers received controlled level scaling and semantic Gen 3-4
  variety replacements without broadly inflating every route trainer.

## Regular Trainer Rules

- Regular trainer party sizes are not broadly inflated.
- No-custom-move regular trainers may receive one or two semantic Gen 3-4
  replacements, such as roadside birds, bugs, fish, cave Pokemon, Rocket poison
  Pokemon, or similar class-appropriate swaps.
- Regular trainers intentionally remain below the late boss/rematch ceiling.

## Validation

- All 866 trainer constants used by the Perfect Johto trainer table are present
  in this fork's headers.
- The trainer source now hash-matches Perfect Johto's `Trainers.c`.
- `make` completed successfully after import and regenerated trainer data,
  trainer party, trainer text, and ROM output.

Runtime route/order playtesting is still required before marking Step 4 stable.
