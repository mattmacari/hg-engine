# Sprout Tower (2F / 3F)

See `documentation/areas/README.md` for what this doc format is and how to reproduce it for other
areas. Covers both floors in one doc since their `EncounterData` entries are byte-identical.

## Header facts

- **ENCDATA constants:** `ENCDATA_D15R0102_SPROUT_TOWER_2F` (`data/Encounters.c:609`),
  `ENCDATA_D15R0103_SPROUT_TOWER_3F` (`data/Encounters.c:709`)
- **Map constants:** `MAP_D15R0102` (`include/constants/maps.h:159`),
  `MAP_D15R0103` (`include/constants/maps.h:160`)
- **Connects:** Inside Violet City. Optional pre-gym content — clearing the tower (Elder's Flash
  TM reward) is not required to challenge Falkner.
- **Biome Map tie-in:** not called out in `HACK_PLAN.md`'s Falkner row (which focuses on the
  approach routes/Dark Cave for type coverage). Thematically this is Violet's Ghost/bug-tower
  flavor — more relevant to Morty (Ecruteak, Ghost gym) as an early taste of the type than to
  Falkner's Flying/Rock/Electric/Ice picture.

## Encounter methods active

| Method | Rate | Active? |
|---|---|---|
| Walk | 5 | Yes (low — indoor floor, sparse encounters) |
| Surf | 0 | No |
| Rock Smash | 0 | No |
| Old Rod | 0 | No |
| Good Rod | 0 | No |
| Super Rod | 0 | No |

## Land encounter table (walk, rate 5) — identical on both floors

| Slot | % | Level | Morning | Day | Night |
|---|---|---|---|---|---|
| 1 | 20 | 3 | Sentret | Sentret | Gastly |
| 2 | 20 | 4 | Sentret | Sentret | Gastly |
| 3 | 10 | 3 | Sentret | Sentret | Gastly |
| 4 | 10 | 4 | Sentret | Sentret | Gastly |
| 5 | 10 | 5 | Sentret | Sentret | Gastly |
| 6 | 10 | 5 | Sentret | Sentret | Gastly |
| 7 | 5 | 3 | Sentret | Sentret | Sentret |
| 8 | 5 | 3 | Sentret | Sentret | Sentret |
| 9 | 4 | 6 | Sentret | Sentret | Gastly |
| 10 | 4 | 5 | Sentret | Sentret | Sentret |
| 11 | 1 | 6 | Sentret | Sentret | Gastly |
| 12 | 1 | 5 | Sentret | Sentret | Sentret |

Morning and Day are 100% Sentret — this floor is Sentret-only outside of the night pool.

## Rustling grass (Hoenn/Sinnoh sound species)

| Region | Slot 1 | Slot 2 |
|---|---|---|
| Hoenn | Zigzagoon | Spinda |
| Sinnoh | Chatot | Meditite |

## Swarm

- `landSwarm = SPECIES_SENTRET`
- **Inert:** neither `MAP_D15R0102` nor `MAP_D15R0103` is in `sSwarmMapLUT` (`src/swarms.c`).

## Species summary

| Species | Type(s) | Regional Dex # | Method | Time |
|---|---|---|---|---|
| Sentret | Normal | 15 | Walk | Morning/Day/Night |
| Gastly | Ghost/Poison | 51 | Walk | Night |
| Zigzagoon | Normal | **not in regional dex** | Rustling grass (Hoenn) | — |
| Spinda | Normal | **not in regional dex** | Rustling grass (Hoenn) | — |
| Chatot | Normal/Flying | **not in regional dex** | Rustling grass (Sinnoh) | — |
| Meditite | Fighting/Psychic | **not in regional dex, sheet decision still `Maybe`** | Rustling grass (Sinnoh) | — |

Dex numbers as of the full sheet-sync pass (`data/RegionalDex.c`, 366 entries) — re-`grep` if the
dex is renumbered again before this area's table is finalized.

## Notes

- **Resolved — Rattata → Sentret**, across every slot it appeared in (Morning ×12, Day ×12, Night
  ×4 at slots 7/8/10/12, plus `landSwarm`). Sentret was chosen over a fresh species for this
  100%-share replacement specifically because it's low-risk: same Normal typing (no ripple into
  Falkner's Rock/Electric/Ice coverage audit), already dex-tracked (#15), lower BST (215) than
  Rattata's (253) so no power increase even at full pool share, and already reused on Routes
  29–31 so this adds no new species to track.
- Gastly (Ghost) fits the tower's flavor and is already dex-tracked (#51) — no issue there.
- **Meditite is a genuine open decision, not a routine cut** — unlike the other dex-less species
  on this floor, the curation sheet has it as `keep=Maybe`, not `No`. Worth surfacing when the
  115 open "Maybe" decisions get worked through, rather than treating it as settled.
- Optional/non-critical-path status means this floor is lower priority than Routes 29–31 + Dark
  Cave for the Falkner type-coverage audit — flagged here for completeness, not because it needs
  fixing before Falkner's roster work starts.
