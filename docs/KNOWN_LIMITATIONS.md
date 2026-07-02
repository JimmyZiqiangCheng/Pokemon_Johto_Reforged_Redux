# Known Limitations

## Phase 1

- EV/IV summary viewer is disabled due known UI hook instability in the
  abandoned project.
- Summary nature arrows/colors and mint-aware nature stat hooks are disabled
  because they touch the same stat-page path as the unstable EV/IV viewer.
- Save expansion, expanded PC boxes, and expanded item pockets are disabled.
- Mega Evolution and Primal Reversion are disabled.
- Custom party item-use hooks are disabled.
- Wild Pokemon post-processing hooks are disabled.
- HG-engine-added save/general text is deferred where it shifts vanilla save UI
  message IDs. Reusable Repel text is appended at safe bank 40 IDs instead.
- HG-engine-added battle text is deferred where it shifts vanilla battle UI
  message IDs.
- Mart and item economy changes are not included.
- Running Shoes script edits and Cherrygrove Guide skip are not included.
- No Pokemon data, encounter, trainer, item, or postgame design changes have
  been applied yet.

## Required Manual Testing

Static build success does not prove runtime stability. Each release still needs
manual boot, early-game, party menu, summary, bag, PC, and first wild encounter
checks.

Run `python tools\johto_reforged\validate_phase1_stable_hooks.py` after phase 1
builds to confirm the deferred UI/runtime hooks are restored to clean bytes and
that save screen, battle command, move PP, party menu, and summary screen text
IDs are still aligned to clean HeartGold. The same validator also checks the
reusable Repel common-script text remap.
