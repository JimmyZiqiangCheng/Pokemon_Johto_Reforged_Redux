# Encounter Systems

This is the Step 3 reference for ordinary wild tables, rare finds, Safari and
Headbutt support, natural wild hidden-ability rolling, and the disabled random
roaming legendary source design.

## Source Files

- Main wild encounters: `hg-engine-main/data/Encounters.c`.
- Safari encounters: `hg-engine-main/data/SafariEncounters.c`.
- Headbutt encounters: `hg-engine-main/data/Headbutt.c`.
- Encounter slot rolls: `hg-engine-main/src/field/encounter_check.c`.
- Wild encounter baseline hook: `hg-engine-main/src/field/enemy_party.c`.

## Implemented Step 3 Scope

- Main wild encounter tables are imported from the Perfect Johto reference.
- Safari encounter tables are imported from the Perfect Johto reference.
- Headbutt encounters already matched the Perfect Johto reference.
- Rare finds are implemented through low-rate table slots rather than a separate
  runtime system.
- Rare finds are compiled into `Encounters.c`/`SafariEncounters.c`; they are
  direct encounter-table placements and are independent from the random roaming
  legendary overlay.
- The HG-engine/Generations baseline wild hook is active for held items,
  passive forms, Unown forms, scripted hidden abilities, and natural wild
  hidden-ability rolling through `NATURAL_WILD_HIDDEN_ABILITIES`.
- Random roaming legendary surprise encounters are disabled after the
  `v0.5.3-roamers-availability-test` crash report. The source design remains
  documented, but `RANDOM_LEGENDARY_ROAMING_ENCOUNTERS` is compiled out.

## Reference Docs

- Main wild tables: `docs/WILD_ENCOUNTERS.md`.
- Rare-find layer: `docs/RARE_ENCOUNTERS.md`.
- Random roaming legendary encounters: `docs/RANDOM_LEGENDARY_SYSTEM.md`.
