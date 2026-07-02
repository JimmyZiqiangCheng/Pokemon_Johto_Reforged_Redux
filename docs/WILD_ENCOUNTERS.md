# Wild Encounters

Wild encounters are the main one-save obtainability layer for ordinary Pokemon.
Step 3 imports the Perfect Johto main wild and Safari encounter tables.

## Rules Adopted From Perfect Johto

- Main land encounters use a shared daytime pool: morning and day are identical,
  while night remains separate.
- Meaningful land/cave pools and surf/fishing pools should have at least six
  species when that encounter mode exists.
- Johto routes and dungeons include Generation 3-4 Pokemon as normal ecology,
  not only as rare prizes.
- Late-Johto, Kanto, and postgame encounter levels are raised to match stronger
  progression.
- Starter families are pushed into late-game or postgame contexts.
- Non-rare low-rate filler slots duplicate common species so future tools do not
  treat ordinary filler as rare finds.

## Source Reference

- Imported main table:
  `<romhack-workspace>\perfect_johto\hg-engine-main\hg-engine-main\data\Encounters.c`.
- Imported Safari table:
  `<romhack-workspace>\perfect_johto\hg-engine-main\hg-engine-main\data\SafariEncounters.c`.
- Headbutt table already matched:
  `<romhack-workspace>\perfect_johto\hg-engine-main\hg-engine-main\data\Headbutt.c`.

## Final Availability Audit

Last checked on 2026-07-02 against the current `Encounters.c`,
`SafariEncounters.c`, and `Headbutt.c`.

- Main encounter entries parsed: 142.
- Meaningful non-Safari encounter areas: 132.
- Meaningful areas with at least six encounter species: 132 / 132.
- Meaningful land/cave pools with at least six species: 108 / 108.
- Meaningful surf/fishing pools with at least six species: 71 / 71.
- Species placed across main wild, Safari, and Headbutt sources: 312.
- Non-legendary Gen 1-4 evolution-family components covered: 211 / 211.
- Missing non-legendary Gen 1-4 family components: none.
- Missing non-legendary Gen 1-4 base/pre-evolution species: none.
- Unrelated later-generation species in encounter tables: none.
- Non-starter Gen 3-4 base/pre-evolution species covered in Johto main
  encounters: 95 / 95.
- Approved later regional base-form placements covered: 19 / 19.
- Approved later direct-evolution families connected to Gen 1-4 bases have wild
  pre-evolution/base-family coverage: yes.
- Perfect Johto-style encounter validation errors: 0.
- Perfect Johto in-memory regeneration renders back to the current
  `Encounters.c` exactly.

Legendary and mythical Pokemon are excluded from the ordinary wild availability
count. Their repeatable access is tracked separately in
`RANDOM_LEGENDARY_SYSTEM.md`.
