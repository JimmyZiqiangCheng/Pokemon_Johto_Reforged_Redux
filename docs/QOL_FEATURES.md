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
- EV/IV summary viewer through `IMPLEMENT_NEW_EV_IV_VIEWER`, using appended
  runtime summary text IDs 195-212 so vanilla summary labels stay aligned.

## Deferred

- Separate mint-aware nature stat override hooks.
- Expanded PC boxes and expanded bag pockets.
- Custom party-use behavior for mints, Ability Capsule, Ability Patch, IV
  candies, Max Candy, and repeat-use candies.
- Broader wild form post-processing.
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
code reads the expected labels. The EV/IV viewer is allowed only because its
extra labels are appended to summary archive 302 instead of shifting or
reusing vanilla labels. Battle text archive 197 must also preserve
clean HeartGold IDs for the command menu and move PP labels. Save/general text
archive 40 must preserve clean HeartGold IDs for the save prompt and Hall of
Fame warning.

Reusable Repels are the exception that still needs new text in phase 1. The
Repel prompt is appended to bank 40 at message ID 234 and the "used" message is
appended at ID 236. The common script is remapped to those appended IDs, so no
vanilla save-screen IDs shift.
