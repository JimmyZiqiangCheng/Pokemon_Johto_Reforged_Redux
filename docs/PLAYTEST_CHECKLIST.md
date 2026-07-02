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
- On a Pokemon summary stat page, `L` shows EVs, `R` shows IVs, and `SELECT`
  returns to normal stats without corrupting labels.

## Phase 2 Pokemon Data Checks

- Summary data for spot-check species shows imported stats, typing, and
  abilities from Perfect Johto.
- Level-up move learning works for early-game and evolved Pokemon.
- Known-move evolutions for Stantler, Primeape, and Galarian Farfetch'd trigger
  when the required move is known.
- Trade-replacement and trade-with-item replacement evolutions trigger through
  their imported non-trade methods when the required item is available.
- Dudunsparce Three-Segment and Ursaluna Bloodmoon evolution paths should be
  runtime-tested for form display and naming.
- Scripted hidden-ability encounters still work when a script sets the hidden
  ability flag.
- Ordinary wild Pokemon can roll hidden abilities as another normal ability
  slot; catch spot checks should confirm hidden ability species can appear
  naturally without corrupting ability, form, or stats.

## Phase 3 Wild Encounter Checks

- Route 29 daytime encounters include Zigzagoon, Starly, Bidoof, Sentret,
  Pidgey, and rare Houndour.
- Early surf/fishing rare slots appear at the expected low rate without
  replacing common encounter flow.
- Rod slot 4 behaves as the 4% rare/filler slot.
- Safari Zone encounters load without table corruption.
- Random roaming legendaries are disabled in this isolation build after the
  `v0.5.3-roamers-availability-test` crash report.
- First wild encounter does not freeze.
- Several ordinary wild encounters can start and reach the battle command menu
  without crashing.

## Phase 4 Trainer Checks

- Falkner, Bugsy, Whitney, Morty, Chuck, Jasmine, Pryce, and Clair load with
  six-Pokemon first-clear teams at their documented level bands.
- First Elite Four and Lance load six-Pokemon teams from Will 50-54 through
  Lance 58-60.
- Kanto leaders load post-League teams, ending with Blue 78-82.
- Gym Leader rematches, Elite Four rematches, Lance rematches, Red, and
  late-postgame challenge records load without trainer-data or text corruption.
- Major Silver, Rocket Executive, and Giovanni/Rocket Boss fights have the
  expanded teams expected at their story points.
- Regular route, cave, sea, gym non-leader, and Rocket trainers preserve local
  pacing without severe difficulty spikes.
- Trainer last-Pokemon, half-HP, win, lose, and phone-rematch text still renders
  correctly for spot-check bosses and rematch trainers.

## Phase 5 Item And Mart Checks

- Standard mart stock changes as badges are obtained.
- 0-badge standard marts show only the early essentials from the badge mart.
- At 3 badges, feathers, EV-reduction berries, mints, and Ability Capsule are
  stocked.
- At 4 badges, vitamins, common stones, Oval Stone, and Linking Cord are
  stocked.
- At 5 badges, IV stat candies, Macho Brace, Power items, and trade-item
  replacements are stocked.
- At 6 badges, Ability Patch and broader evolution items are stocked.
- Max Candy does not appear before 12 badges and appears at 12+ badges.
- Badge-stocked items display correct names, icons, prices, and pockets.
- Item-use behavior for mints, Ability Capsule/Patch, IV candies, and Max Candy
  should be tested before enabling `IMPLEMENT_PARTY_ITEM_USE_OVERRIDES`.

## Phase 6 Postgame Checks

- Saffron Fighting Dojo master opens the postgame hub after 8 badges.
- All 16 visible Gym Leader rematch NPCs still appear and battle correctly
  through the Dojo phone-rematch flow.
- Elite Four rematch teams load correctly through the League flow.
- Champion Circuit Lance and Blue unlock after 16 badges.
- Champion Circuit Red, Steven, Wallace, and Cynthia unlock after Red is
  defeated on Mt. Silver.
- Dossier battles set caught flags only on capture and remain retryable after a
  flee, faint, or player loss.
- Regigigas, Rayquaza, Darkrai, Phione, and Arceus prerequisite chains block and
  open correctly.

## Regression Checks

- Party menu labels show `SWITCH`, `SUMMARY`, `ITEM`, and `QUIT`, not party
  order or compatibility labels.
- Summary screen stat, Ability, PP, move Power, Accuracy, and Category labels
  are sane.
- Summary EV/IV stat labels show HP, Attack, Defense, Sp. Atk, Sp. Def, Speed,
  EV, and IV rather than personality, move, or ability text.
- Battle move buttons show PP values and `PP`, not `BAIT`, `Quit`, or move
  deletion prompt text.
- Save screen prompt asks to save the game and does not show the Hall of Fame
  corruption warning.
- Reusable Repel prompt does not alter the save-screen text, battle move
  buttons, party menu labels, or summary labels.
- Bag item labels are sane.
- PC storage opens and behaves as 18-box vanilla storage.
