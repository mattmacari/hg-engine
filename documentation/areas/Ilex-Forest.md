# Ilex Forest

See `documentation/areas/README.md` for what this doc format is and how to reproduce it for other
areas.

## Header facts

- **ENCDATA constant:** `ENCDATA_D36R0101_ILEX_FOREST` (`data/Encounters.c:2009`)
- **Map constant:** `MAP_D36R0101` (`include/constants/maps.h:121`)
- **Connects:** Azalea Town (north) ↔ Route 34 (south, toward Goldenrod/Whitney).
- **Leads toward:** named explicitly in `HACK_PLAN.md`'s Bugsy row, even though it's geographically
  the exit route *after* Azalea Town rather than an approach route.
- **Biome Map tie-in:** `HACK_PLAN.md`'s Bugsy row: "Ilex Forest is already a deep-forest biome —
  canon-correct, just deepen bug variety (Scyther/Pinsir via Headbutt trees)." Scyther/Pinsir are
  **Headbutt-tree** encounters (`data/Headbutt.c`) — a separate struct from `EncounterData` per
  `documentation/Encounter-Data-Structure.md` — see the Headbutt trees section below; done as part
  of this area's Bugsy-approach pass alongside the `EncounterData` audit above.

## Encounter methods active

| Method | Rate | Active? |
|---|---|---|
| Walk | 5 | Yes |
| Surf | 15 | Yes |
| Rock Smash | 0 | No |
| Old Rod | 25 | Yes |
| Good Rod | 50 | Yes |
| Super Rod | 75 | Yes |

## Land encounter table (walk, rate 5)

| Slot | % | Level | Morning | Day | Night |
|---|---|---|---|---|---|
| 1 | 20 | 5 | Caterpie | Caterpie | Oddish |
| 2 | 20 | 6 | Metapod | Caterpie | Oddish |
| 3 | 10 | 5 | Caterpie | Caterpie | Oddish |
| 4 | 10 | 6 | Metapod | Caterpie | Oddish |
| 5 | 10 | 6 | Caterpie | Metapod | Zubat |
| 6 | 10 | 6 | Caterpie | Metapod | Zubat |
| 7 | 5 | 5 | Paras | Metapod | Paras |
| 8 | 5 | 5 | Paras | Metapod | Paras |
| 9 | 4 | 5 | Zubat | Zubat | Zubat |
| 10 | 4 | 6 | Paras | Paras | Paras |
| 11 | 1 | 5 | Zubat | Zubat | Zubat |
| 12 | 1 | 6 | Paras | Paras | Paras |

## Water/rod tables

**Surf (rate 15):** Psyduck ×2 (10–20/5–15, 60/30%), Golduck ×3 (10–20/10–20/10–20, 5/4/1%) — this
table is entirely the Psyduck line.
**Old Rod (60/30/5/4/1):** Magikarp ×3, Poliwag ×2 (all level 10).
**Good Rod (40/40/15/4/1):** Magikarp, Poliwag ×4 (all level 20).
**Super Rod (40/40/15/4/1):** Poliwag ×2, Magikarp, Poliwag, Magikarp (all level 40).

## Rustling grass (Hoenn/Sinnoh sound species)

| Region | Slot 1 | Slot 2 |
|---|---|---|
| Hoenn | Spoink | Numel |
| Sinnoh | Budew | Carnivine |

## Swarm

- `landSwarm = SPECIES_CATERPIE`, `surfSwarm = SPECIES_PSYDUCK`.
- **Inert:** `MAP_D36R0101` is not in `sSwarmMapLUT` (`src/swarms.c`).

## Headbutt trees (`data/Headbutt.c`, `HeadbuttFile_117_Ilex_Forest`)

56 normal trees, 0 special trees.

| Slot | Level | Species |
|---|---|---|
| 1 | 3–5 | Hoothoot |
| 2 | 3–5 | Caterpie |
| 3 | 3–5 | Caterpie |
| 4 | 3–5 | Hoothoot |
| 5 | 3–5 | Metapod |
| 6 | 3–5 | Metapod |
| 7 | 6–8 | Hoothoot |
| 8 | 6–8 | Scyther |
| 9 | 6–8 | Pinsir |
| 10 | 6–8 | Noctowl |
| 11 | 6–8 | Butterfree |
| 12 | 6–8 | Butterfree |

**Resolved — Bug-variety deepening per `HACK_PLAN.md`'s Bugsy row.** Replaced the two duplicate
Pineco slots (8/9, level 6–8) with Scyther and Pinsir. Both are already Bug/canon Ilex Forest
headbutt-tree species in the mainline games (version-exclusive there; not version-locked here since
this is a single build). Pinsir required a dex-curation change — see Notes.

## Species summary

| Species | Type(s) | Regional Dex # | Method | Time |
|---|---|---|---|---|
| Caterpie | Bug | 20 | Walk/Headbutt | Morning/Day |
| Metapod | Bug | 21 | Walk/Headbutt | Morning/Day |
| Paras | Bug/Grass | 63 | Walk | Morning/Day/Night |
| Oddish | Grass/Poison | 68 | Walk | Night |
| Poliwag | Water | 346 | Fish | — |
| Magikarp | Water | 65 | Fish | — |
| Spoink | Psychic | 224 | Rustling grass (Hoenn) | — |
| Hoothoot | Normal/Flying | 13 | Headbutt | — |
| Noctowl | Normal/Flying | 14 | Headbutt | — |
| Butterfree | Bug/Flying | 22 | Headbutt | — |
| Scyther | Bug/Flying | 86 | Headbutt | — |
| Pinsir | Bug | 368 | Headbutt | — |
| Zubat | Poison/Flying | **not in regional dex** | Walk | Night (also slots 9/11 day/morning) |
| Psyduck | Water | **not in regional dex** | Surf | — |
| Golduck | Water | **not in regional dex** | Surf | — |
| Numel | Fire/Ground | **not in regional dex** | Rustling grass (Hoenn) | — |
| Budew | Grass/Poison | **not in regional dex** | Rustling grass (Sinnoh) | — |
| Carnivine | Grass | **not in regional dex** | Rustling grass (Sinnoh) | — |

Dex numbers as of the full sheet-sync pass (`data/RegionalDex.c`, 368 entries) — re-`grep` if the
dex is renumbered again before this area's table is finalized.

## Notes

- Zubat/Psyduck/Golduck dex-less here is the same routine curation-sheet cut seen throughout the
  Bugsy approach (`keep = No`) — not a bug. Worth noting the surf table specifically: with both
  Psyduck and Golduck cut, Ilex Forest's entire water-encounter method is currently 100% dex-less.
- **Resolved — Fire-counter gap closed on Route 33, not here.** Growlithe was added to Route 33
  (the last approach route before Bugsy) instead of promoting Numel; Numel stays as the existing
  Hoenn rustling-grass "surprise" species, unchanged, since it's geographically past the gym anyway.
- **Resolved — dex-curation decision for Pinsir.** Pinsir was `keep = No` (Kanto-only in vanilla)
  in `data/generated/species_dex_meta.csv`; flipped to `Yes` with a note explaining the move, since
  `HACK_PLAN.md` explicitly calls for it in Johto's Ilex Forest. Added to `data/RegionalDex.c` as
  #368 (appended, per the file's existing append-order convention). Scyther and Hoothoot/Noctowl/
  Butterfree were already dex-tracked, no curation change needed for them.
- **Bug variety deepened via Headbutt trees, not this table** — see the Headbutt trees section
  above. `data/Encounters.c`'s own walk table stays Caterpie/Metapod/Paras-only, matching
  `HACK_PLAN.md`'s framing that the Scyther/Pinsir work belongs to the Headbutt struct, not here.
- Oddish (Grass/Poison) appearing only at night is the one non-Bug/Water species on this table —
  matches vanilla's "forest floor bloom at night" flavor, no issue.
