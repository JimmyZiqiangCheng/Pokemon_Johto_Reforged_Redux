# Legendaries

Phase 6 implements proper Gen 1-4 legendary and mythical access through native
roamers plus Saffron Fighting Dojo dossier battles.

## Access Layers

- Raikou and Entei remain native Burned Tower roamers.
- Articuno, Zapdos, and Suicune dossier battles open after 8 badges.
- The remaining dossiers open after 16 badges unless they have an extra
  prerequisite.
- Dossier caught flags are set only when static encounter outcome `4` is
  returned, so failed, fled, or fainted attempts stay retryable.
- Latias and Latios use Phase 8 dossier flags separate from native roamer state.

## Prerequisite Chains

- Regirock, Regice, and Registeel before Regigigas.
- Kyogre and Groudon before Rayquaza.
- Cresselia before Darkrai.
- Manaphy before Phione.
- Red defeated plus Uxie, Mesprit, Azelf, Dialga, Palkia, and Giratina before
  Arceus.

## Coverage

- Native roamers: Raikou, Entei.
- Dojo dossiers: Articuno, Zapdos, Moltres, Mewtwo, Lugia, Ho-Oh, Suicune,
  Latias, Latios, Regirock, Regice, Registeel, Regigigas, Kyogre, Groudon,
  Rayquaza, Mew, Celebi, Jirachi, Deoxys, Heatran, Cresselia, Darkrai,
  Shaymin, Manaphy, Phione, Uxie, Mesprit, Azelf, Dialga, Palkia, Giratina,
  Arceus.

The separate random legendary wild overlay is disabled after the
`v0.5.3-roamers-availability-test` crash report and is documented in
`docs/RANDOM_LEGENDARY_SYSTEM.md`. Dojo dossiers remain the deterministic
capture route for controlled legendary/mythical access.
