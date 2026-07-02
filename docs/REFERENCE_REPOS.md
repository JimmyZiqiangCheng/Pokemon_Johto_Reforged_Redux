# Reference Repos

This project uses external repos as read-only implementation references. Do not
vendor them into this repository and do not port changes directly without
checking Johto Reforged's local text IDs, hook gates, save layout, and current
phase scope.

## HeartGold Generations 2.0

Purpose: HG-engine implementation reference for QOL features and modernized
HeartGold behavior.

- GitHub:
  `https://github.com/spearmintz1/hg-engine/tree/HeartGold-Generations-%28Full-Version-2.0%29`
- Local clone:
  `<romhack-workspace>\reference_repos\heartgold_generations_hg_engine_2_0`
- Branch:
  `HeartGold-Generations-(Full-Version-2.0)`
- Current local commit:
  `c28e104a8ed664ce1a5dba6b0d8d83caded89b62`
- Upstream remote:
  `https://github.com/spearmintz1/hg-engine.git`

Recreate the local clone if needed:

```powershell
git clone --recursive --branch "HeartGold-Generations-(Full-Version-2.0)" https://github.com/spearmintz1/hg-engine.git <romhack-workspace>\reference_repos\heartgold_generations_hg_engine_2_0
```

Useful files to compare:

- `CONFIG.md`: documents HG-engine feature flags.
- `include/config.h`: enabled feature set in Generations.
- `hooks`: hook sites and config gates.
- `src/summary.c`: EV/IV summary viewer behavior.
- `data/text/302.txt`: summary-screen text archive layout.

Porting notes:

- Treat Generations as a behavior reference, not a drop-in source of truth.
- Text archive IDs are especially dangerous. Generations' summary viewer used
  IDs that did not match Johto Reforged's restored text archive layout. Johto
  Reforged now keeps appended EV/IV labels in archive 302 runtime IDs 195-212.
- Decode or validate text archives before wiring code to message IDs. The
  physical source rows in `data/text/*.txt` are not always the same as runtime
  message IDs after `msgenc` processing.
- Do not enable Generations' save expansion, expanded PC boxes, or expanded bag
  pockets in Johto Reforged without a separate boot/save compatibility pass.
  Those areas overlap with previously unstable save-layout changes.
- Keep party context UI overrides, custom party item-use overrides, and broad
  wild post-processing changes behind local Johto Reforged config gates until
  they are tested independently.
