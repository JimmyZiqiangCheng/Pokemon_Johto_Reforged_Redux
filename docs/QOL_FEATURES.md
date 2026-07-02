# QOL Features

This document tracks the phase 1 QOL baseline.

## Enabled In Phase 1

- Fast text through `FAST_TEXT_PRINTING`.
- Reusable TMs through `REUSABLE_TMS`.
- Deletable HMs through `DELETABLE_HMS`.
- Capture EXP through `IMPLEMENT_CAPTURE_EXPERIENCE`.
- Critical captures through `IMPLEMENT_CRITICAL_CAPTURE`.
- Hidden Abilities support through `HIDDEN_ABILITIES`.
- Reusable Repels through `IMPLEMENT_REUSABLE_REPELS`.
- Updated vitamin EV caps through `UPDATE_VITAMIN_EV_CAPS`.
- Disabled overworld poison damage through `UPDATE_OVERWORLD_POISON`.
- Anti-piracy patching through `APPLY_ANTIPIRACY`.

## Deferred

- EV/IV summary viewer, nature stat arrows/colors, and mint-aware nature stat
  hooks.
- Expanded PC boxes and expanded bag pockets.
- Custom party-use behavior for mints, Ability Capsule, Ability Patch, IV
  candies, Max Candy, and repeat-use candies.
- Natural wild hidden ability/form post-processing.
- Running Shoes script edits and Cherrygrove Guide skip.
- AutoRun or toggle-run.
- Fast Surf.
- Field moves without teaching HMs.
- Mart and item economy changes.

## Stability Notes

The previous `perfect_johto` build rolled back summary UI, party menu, expanded
save, and wild post-processing hooks after runtime instability. Phase 1 keeps
those systems disabled until they can be tested independently. Party menu and
summary text archives must preserve clean HeartGold message IDs so vanilla UI
code reads the expected labels. Battle text archive 197 must also preserve
clean HeartGold IDs for the command menu and move PP labels. Save/general text
archive 40 must preserve clean HeartGold IDs for the save prompt and Hall of
Fame warning.
