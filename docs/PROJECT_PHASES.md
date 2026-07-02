# Project Phases

## Phase 1 - Initial HG-Engine QOL Build

Goal: produce a clean HG-engine ROM and patch with only important, low-risk QOL
features enabled.

Included:

- HG-engine baseline build from a clean US HeartGold ROM.
- Conservative config cleanup for stability.
- Reusable Repel prompt restored through appended text IDs and script remapping.
- Versioned `release/` output.
- Documentation structure for future phases.

Excluded:

- Pokemon stat, ability, move, typing, and evolution design changes.
- Wild encounters, trainer rosters, item economy, mart stock, and postgame
  systems.
- Runtime mode selection, level caps, Nuzlocke rules, random legendary systems,
  and custom party item-use behavior.

## Phase 2 - Pokemon Data

Apply Pokemon stats, abilities, moves, typing, evolution, and learnset changes.
Each data source and design exception should be documented before release.

Status: implemented in the working tree from the Perfect Johto reference;
release build and runtime playtesting are still required.

## Phase 3 - Wild Encounters

Apply wild encounter table changes and validate progression, availability, and
area identity.

Status: implemented in the working tree from the Perfect Johto reference;
release build and runtime playtesting are still required.

## Phase 4 - Trainers

Apply trainer team, boss team, rematch, and level curve updates.

Status: implemented in the working tree from the Perfect Johto reference;
static symbol validation and local build passed, runtime playtesting is still
required.

## Phase 5 - Items

Apply item behavior, mart stock, economy, and customization item changes.

Status: implemented in the working tree from the Perfect Johto reference; local
build and static item validation passed. Runtime testing is still required,
especially badge-gated mart stock and config-gated custom party item-use
behavior.

## Phase 6 - Postgame

Expand postgame features, legendary access, rematches, and optional late-game
challenge content.

Status: implemented in the working tree from the Perfect Johto Phase 8
reference; Dojo script assembly and static postgame validation passed. Runtime
testing is still required for Dojo menus, rematch visibility, dossier battles,
caught flags, and Champion Circuit unlock gates.
