# Playtest Checklist

Use this checklist before marking a phase release stable.

## Boot Smoke Test

- ROM reaches the title screen.
- New game can begin.
- Intro text renders correctly.
- First player movement works.
- Save and reload work with vanilla save sizing.

## Phase 1 QOL Checks

- Text prints quickly.
- TMs are reusable after teaching.
- HMs can be deleted or forgotten.
- Capturing a Pokemon grants EXP.
- Critical captures can trigger without visual corruption.
- Repel reuse prompt appears after a Repel expires and the follow-up "used"
  message names the selected Repel correctly.
- Overworld poison does not damage the party while walking.
- Vitamins can pass the vanilla 100 EV per-stat cap up to the updated cap.

## Regression Checks

- Party menu labels show `SWITCH`, `SUMMARY`, `ITEM`, and `QUIT`, not party
  order or compatibility labels.
- Summary screen stat, Ability, PP, move Power, Accuracy, and Category labels
  are sane.
- Battle move buttons show PP values and `PP`, not `BAIT`, `Quit`, or move
  deletion prompt text.
- Save screen prompt asks to save the game and does not show the Hall of Fame
  corruption warning.
- Reusable Repel prompt does not alter the save-screen text, battle move
  buttons, party menu labels, or summary labels.
- First wild encounter does not freeze.
- Bag item labels are sane.
- PC storage opens and behaves as 18-box vanilla storage.
