# Items And Marts

This doc covers the Phase 5 badge-gated mart economy, customization items, IV
candies, Max Candy, and evolution-item access.

## References

- Phase source: `<romhack-workspace>\perfect_johto`.
- Badge mart source: `hg-engine-main/src/field/mart.c`.
- Item data: `hg-engine-main/data/itemdata/itemdata.c`.
- Item constants: `hg-engine-main/include/constants/item.h` and
  `hg-engine-main/asm/include/items.inc`.
- Party-use behavior source:
  `hg-engine-main/src/individual/PartyMenu_HandleUseItemOnMon.c`.
- Evolution methods: `docs/EVOLUTIONS.md`.

## Badge Mart Summary

- Badge mart entries: 104 / 203 UI limit.
- 0-2 badges: core balls, medicine, status heals, Escape Rope, and Repels.
- 3 badges: EV feathers, EV-reduction berries, all available mints, and
  Ability Capsule.
- 4 badges: EV vitamins, common stones, Oval Stone, and Linking Cord.
- 5 badges: IV stat candies, Macho Brace, Power items, and trade-item
  replacements.
- 6 badges: Ability Patch and broad evolution access, including Black Augurite,
  Peat Block, Galarica Cuff, and Galarica Wreath.
- 12 badges: Max Candy.

## Prices And Effects

- Max Candy costs 8000, unlocks at 12 badges, and sets all six IVs to 31 when
  the party item-use override is enabled.
- Health, Mighty, Tough, Smart, Courage, and Quick Candy cost 2000, unlock at
  5 badges, and set one matching IV to 31 when the party item-use override is
  enabled.
- Mints, Ability Capsule, and Ability Patch cost 1000 with their intended badge
  gates.
- Vitamins and Power items cost 3000.
- Feathers cost 300.
- EV-reduction berries cost 200.
- Approved-scope evolution items are stocked through the badge mart.

## Runtime Notes

`MART_EXPANSION` is enabled, so standard marts use badge-count stock generation.
The source behavior for mints, Ability Capsule/Patch, IV stat candies, and Max
Candy is present, but the party item-use hook remains controlled by
`IMPLEMENT_PARTY_ITEM_USE_OVERRIDES` because that hook path previously caused
party-menu UI instability. Runtime testing should explicitly decide when that
hook is safe to enable.

## Restrictions

- Forbidden gimmick items are not stocked in the badge mart.
- Unrelated later-family evolution items are not exposed unless needed by an
  approved Gen 1-4 family exception.
- Trainer-battle held-item restoration remains out of scope.
