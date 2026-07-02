# Kanto Postgame

Phase 6 centers Kanto postgame access on the Saffron Fighting Dojo after the
player reaches Kanto and then completes all 16 badges.

## Hub Behavior

- The Dojo master opens a postgame menu after 8 badges.
- Existing visible Gym Leader rematch NPC scripts remain in the Dojo and still
  use the phone-rematch flow.
- Champion Circuit battles open after 16 badges.
- Advanced Champion Circuit battles and Arceus require Red defeated on Mt.
  Silver.
- Legendary and mythical access uses scripted Dojo dossier battles for Gen 1-4
  Pokemon not already handled by native roamer flow.

## Rematches

- All 16 Gym Leader rematches remain available through the Dojo leader NPCs.
- Elite Four and Lance rematch teams are already present in the trainer table
  from Phase 4 and remain available through the League flow.
- Lance, Blue, Red, Steven, Wallace, and Cynthia are repeatable through the
  Champion Circuit.

## References

- `docs/CHAMPION_CIRCUIT.md`
- `docs/LEGENDARIES.md`
- `docs/BOSS_BATTLES.md`
- Perfect Johto Phase 8 postgame implementation.
- Sacred Gold / Storm Silver reference material via the Perfect Johto docs; the
  current stable implementation uses a compact Dojo dossier hub rather than
  bespoke restored map quests.

Runtime testing should check Dojo menus, Gym Leader rematch visibility,
Champion Circuit unlocks, Elite Four rematch availability, dossier retry
behavior, and caught flags.
