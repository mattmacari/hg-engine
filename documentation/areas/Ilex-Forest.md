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
| 5 | 10 | 6 | Caterpie | Metapod | Woobat |
| 6 | 10 | 6 | Caterpie | Metapod | Woobat |
| 7 | 5 | 5 | Paras | Metapod | Paras |
| 8 | 5 | 5 | Paras | Metapod | Paras |
| 9 | 4 | 5 | Woobat | Woobat | Woobat |
| 10 | 4 | 6 | Paras | Paras | Paras |
| 11 | 1 | 5 | Woobat | Woobat | Woobat |
| 12 | 1 | 6 | Paras | Paras | Paras |

## Water/rod tables

**Surf (rate 15):** Marill (10–20), Marill (5–15), Azumarill (10–20), Azumarill (10–20), Azumarill (10–20).
**Old Rod (rate 25):** Magikarp (10), Magikarp (10), Magikarp (10), Poliwag (10), Poliwag (10).
**Good Rod (rate 50):** Magikarp (20), Poliwag (20), Poliwag (20), Poliwag (20), Poliwag (20).
**Super Rod (rate 75):** Poliwag (40), Poliwag (40), Magikarp (40), Poliwag (40), Magikarp (40).

## Rustling grass (Hoenn/Sinnoh sound species)

| Region | Slot 1 | Slot 2 |
|---|---|---|
| Hoenn | Spoink | Numel |
| Sinnoh | Budew | Carnivine |

## Swarm

- `landSwarm = SPECIES_CATERPIE`, `surfSwarm = SPECIES_MARILL`, `nightFish = SPECIES_POLIWAG`, `fishSwarm = SPECIES_MAGIKARP`.
- **Inert:** this map is not in `sSwarmMapLUT` (`src/swarms.c`).

## Species summary

| Species | Type(s) | Regional Dex # | Method | Time |
|---|---|---|---|---|
| Caterpie | Bug | 20 | Walk, Swarm (land) | Morning/Day |
| Metapod | Bug | 21 | Walk | Morning/Day |
| Paras | Bug/Grass | 63 | Walk | Morning/Day/Night |
| Magikarp | Water | 65 | Fish, Swarm (fish) | — |
| Oddish | Grass/Poison | 68 | Walk | Night |
| Marill | Water/Fairy | 102 | Surf, Swarm (surf) | — |
| Azumarill | Water/Fairy | 103 | Surf | — |
| Spoink | Psychic | 224 | Rustling grass (Hoenn) | — |
| Woobat | Psychic/Flying | 276 | Walk | Morning/Day/Night |
| Poliwag | Water | 346 | Fish, Fish (night) | — |
| Budew | Grass/Poison | **not in dex** | Rustling grass (Sinnoh) | — |
| Carnivine | Grass | **not in dex** | Rustling grass (Sinnoh) | — |
| Numel | Fire/Ground | **not in dex** | Rustling grass (Hoenn) | — |

Dex numbers as of `data/RegionalDex.c` with 377 entries —
re-`grep` if the dex is renumbered.

## Notes

- **Resolved — early-game cleanup pass (after the Clair pass).**
  - Zubat → **Woobat** (#276).
  - Psyduck/Golduck → **Marill/Azumarill** (#102/#103) on surf and the surf swarm, a freshwater
    forest pond pairing that matches the Route 42/Mt. Mortar pool.
  - Ilex Forest's water is no longer 100% dex-less.
  Earlier notes below that describe these species as dex-less or intentionally kept are superseded.
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
