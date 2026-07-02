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
- Repel reuse prompt appears after a Repel expires.
- Overworld poison does not damage the party while walking.
- Vitamins can pass the vanilla 100 EV per-stat cap up to the updated cap.

## Regression Checks

- Party menu labels are sane.
- Summary screen labels are sane.
- First wild encounter does not freeze.
- Bag item labels are sane.
- PC storage opens and behaves as 18-box vanilla storage.
