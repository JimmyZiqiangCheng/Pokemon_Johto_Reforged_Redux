# Known Limitations

## Phase 1

- EV/IV summary viewer is re-enabled with appended summary archive 302 text
  IDs; it still needs manual runtime checks on real summary screens.
- Separate mint-aware nature stat hooks remain disabled.
- Save expansion, expanded PC boxes, and expanded item pockets are disabled.
- Mega Evolution and Primal Reversion are disabled.
- Custom party item-use hooks are disabled.
- Broad HG-engine wild Pokemon post-processing remains disabled through
  `IMPLEMENT_WILD_MON_POSTPROCESSING_HOOK`.
- The Generations baseline wild hook is enabled through
  `IMPLEMENT_GENERATIONS_WILD_MON_HOOK`.
- HG-engine-added save/general text is deferred where it shifts vanilla save UI
  message IDs. Reusable Repel text is appended at safe bank 40 IDs instead.
- HG-engine-added battle text is deferred where it shifts vanilla battle UI
  message IDs.
- Running Shoes script edits and Cherrygrove Guide skip are not included.

## Phase 2

- Pokemon data now matches the Perfect Johto reference for species personal
  data, hidden abilities, evolutions, baby species mappings, and active
  learnsets.
- Move data already matched Perfect Johto before Phase 2.
- Evolution methods that require items are in the data, and repeatable mart
  access for approved-scope evolution items is now provided by Phase 5.
- Broader wild post-processing hooks remain deferred for runtime stability, but
  natural wild hidden ability rolling is restored through the
  Generations-aligned wild hook.
- The badge-gated random roaming legendary overlay is disabled after the
  `v0.5.3-roamers-availability-test` crash report.
- Runtime tests still need to confirm changed typings, abilities, learnsets,
  evolution behavior, and approved special-form display in a built ROM.

## Phase 3

- Main wild and Safari encounter tables are imported from the Perfect Johto
  reference; Headbutt already matched that reference.
- Rare finds are table-slot placements, not a separate runtime encounter type.
- Random roaming legendary source logic remains in the tree but is compiled out
  after the `v0.5.3-roamers-availability-test` crash report.

## Phase 4

- Trainer teams, boss teams, rematches, and the level curve are imported from
  the Perfect Johto reference.
- Static constant validation and local build passed after the import.
- Runtime tests still need to confirm route/order pacing, trainer text,
  rematches, Red, Rocket/Silver pacing, and late-postgame unlock timing.

## Phase 5

- Badge-gated mart stock, item prices, Max Candy item data, and IV/Max candy
  source behavior are imported from the Perfect Johto reference; local build
  and static item validation passed.
- Runtime tests still need to confirm badge-count mart stock, item icons, item
  pockets, prices, and purchase flow in a built ROM.
- Custom party item-use hooks remain config-gated by
  `IMPLEMENT_PARTY_ITEM_USE_OVERRIDES` until party-menu runtime stability is
  proven.

## Phase 6

- Saffron Fighting Dojo postgame script and text are imported from the Perfect
  Johto Phase 8 reference.
- Static validation and direct Dojo script assembly passed.
- Runtime tests still need to confirm Dojo menu flow, all 16 visible Gym Leader
  rematches, Elite Four rematch availability through the League, Champion
  Circuit unlock gates, dossier retry behavior, and caught flags.
- The random legendary wild overlay is disabled after the
  `v0.5.3-roamers-availability-test` crash report. Dojo dossier captures and
  native roamer flow remain the legendary access paths to runtime-test.

## Required Manual Testing

Static build success does not prove runtime stability. Each release still needs
manual boot, early-game, party menu, summary, bag, PC, first wild encounter,
Dojo postgame, and League rematch checks.

Run `python tools\johto_reforged\validate_phase1_stable_hooks.py` after phase 1
builds to confirm the deferred UI/runtime hooks are restored to clean bytes,
that the broad wild replacement and random legendary overlay remain disabled,
and that save screen, battle command, move PP, party menu, and summary screen
text IDs are still aligned to clean HeartGold. The same validator also checks
the reusable Repel common-script text remap and the appended EV/IV summary
labels.
