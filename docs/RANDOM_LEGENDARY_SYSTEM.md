# Random Roaming Legendary System

The random roaming legendary system is a repeatable low-rate overlay on normal
wild encounters. It does not write native roamer save state.

Current status: disabled after the `v0.5.3-roamers-availability-test` crash
report. Natural wild hidden-ability rolling is restored for the next isolation
build, so this overlay is intentionally compiled out through
`RANDOM_LEGENDARY_ROAMING_ENCOUNTERS` being undefined.

## Trigger Flow

- The overlay runs from `AddWildPartyPokemon` after a normal wild encounter has
  already been generated.
- Repel behavior is preserved because the normal encounter flow must succeed
  first.
- Trainer, Safari, native roamer, Pal Park, catching demo, and Bug-Catching
  Contest battles are excluded.
- Generated roaming legendaries receive Teleport in move slot 4 for a
  move-based flee chance.

## Badge Gates And Rates

- 0-3 badges: disabled.
- 4+ badges: weaker/mystical tier can appear at a 1/4000 aggregate tier rate.
- 5+ badges: additional weaker/mystical species enter the pool.
- 6+ badges: cover-worthy tier can appear at a 1/8000 aggregate tier rate.
- 16 badges: mythical late-pool species and Arceus enter their matching tiers.

These are aggregate tier rolls. After a tier succeeds, one currently unlocked
species from that tier is selected.

## Current Source Design Notes

- The roll denominator is 8000.
- Weaker/mystery tier hits twice per denominator, for an aggregate 1/4000 tier
  rate.
- Cover-worthy tier hits once per denominator, for an aggregate 1/8000 tier
  rate.
- The 0-3 badge gate returns before rolling, so badge-less and early-game wild
  encounters cannot be replaced by this overlay.
- The source remains in `enemy_party.c` for later debugging, but the current
  test build excludes it so wild crash testing can focus on the hidden-ability
  path separately.
