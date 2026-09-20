# Route 30

See `documentation/areas/README.md` for what this doc format is and how to reproduce it for other
areas.

## Header facts

- **ENCDATA constant:** `ENCDATA_R30_ROUTE_30` (`data/Encounters.c:309`)
- **Map constant:** `MAP_R30` (`include/constants/maps.h:38`)
- **Connects:** Cherrygrove City ↔ Route 31 (→ Violet City)
- **Leads toward:** Falkner (Violet City) — second leg of the New Bark → Cherrygrove → Route 30 →
  Route 31 → Violet City path.
- **Biome Map tie-in:** `HACK_PLAN.md`'s Falkner entry calls for Rock/Electric/Ice counter access
  on the way in. Route 30 wasn't originally singled out for a specific counter placement (the doc
  suggests Mareep on Route 32 as a secondary Electric path instead), but this route ended up being
  where the Electric gap actually got closed — see the Rattata → Shinx swap in Notes below. Its
  surf table (Poliwag/Poliwhirl) is also worth keeping in mind for Water-leaning options.

## Encounter methods active

| Method | Rate | Active? |
|---|---|---|
| Walk | 25 | Yes |
| Surf | 15 | Yes |
| Rock Smash | 0 | No |
| Old Rod | 25 | Yes |
| Good Rod | 50 | Yes |
| Super Rod | 75 | Yes |

## Land encounter table (walk, rate 25)

| Slot | % | Level | Morning | Day | Night |
|---|---|---|---|---|---|
| 1 | 20 | 2 | Pidgey | Pidgey | Spinarak |
| 2 | 20 | 3 | Caterpie | Caterpie | **Shinx** |
| 3 | 10 | 2 | Pidgey | Pidgey | Spinarak |
| 4 | 10 | 3 | Caterpie | Caterpie | **Shinx** |
| 5 | 10 | 4 | Caterpie | Pidgey | Hoothoot |
| 6 | 10 | 4 | Caterpie | Pidgey | Hoothoot |
| 7 | 5 | 4 | Metapod | Metapod | **Shinx** |
| 8 | 5 | 4 | Metapod | Metapod | **Shinx** |
| 9 | 4 | 4 | Pidgey | Caterpie | Hoothoot |
| 10 | 4 | 4 | Pidgey | Metapod | Hoothoot |
| 11 | 1 | 4 | Pidgey | Caterpie | Hoothoot |
| 12 | 1 | 4 | Pidgey | Metapod | Hoothoot |

## Water/rod tables

**Surf (rate 15):**

| Slot | % | Level | Species |
|---|---|---|---|
| 1 | 60 | 15–25 | Poliwag |
| 2 | 30 | 10–20 | Poliwag |
| 3 | 5 | 15–25 | Poliwhirl |
| 4 | 4 | 15–25 | Poliwhirl |
| 5 | 1 | 32 | Poliwhirl |

**Old Rod (60/30/5/4/1):** Magikarp ×3, Poliwag ×2 (all level 10)
**Good Rod (40/40/15/4/1):** Magikarp, Poliwag ×4 (all level 20)
**Super Rod (40/40/15/4/1):** Poliwag ×2, Magikarp ×2, Poliwag (all level 40)

## Rustling grass (Hoenn/Sinnoh sound species)

| Region | Slot 1 | Slot 2 |
|---|---|---|
| Hoenn | Whismur | Linoone |
| Sinnoh | Buizel | Bidoof |

## Swarm

- `landSwarm = SPECIES_PIDGEY`, `surfSwarm = SPECIES_POLIWAG`, `fishSwarm = SPECIES_MAGIKARP`,
  `nightFish = SPECIES_POLIWAG`
- **Inert:** `MAP_R30` is not in `sSwarmMapLUT` (`src/swarms.c`) — same as Route 29, these fields
  currently do nothing.

## Species summary

| Species | Type(s) | Regional Dex # | Method | Time |
|---|---|---|---|---|
| Pidgey | Normal/Flying | 10 | Walk | Morning/Day/Night |
| Caterpie | Bug | 20 | Walk | Morning/Day |
| Metapod | Bug | 21 | Walk | Morning/Day |
| Spinarak | Bug/Poison | 28 | Walk | Night |
| Shinx | Electric | 235 | Walk | Night |
| Hoothoot | Normal/Flying | 13 | Walk | Night |
| Poliwag | Water | 346 | Surf/Fish | — |
| Poliwhirl | Water | 347 | Surf | — |
| Magikarp | Water | 65 | Fish | — |
| Whismur | Normal | **not in regional dex** | Rustling grass (Hoenn) | — |
| Linoone | Normal | **not in regional dex** | Rustling grass (Hoenn) | — |
| Buizel | Water | **not in regional dex** | Rustling grass (Sinnoh) | — |
| Bidoof | Normal | **not in regional dex** | Rustling grass (Sinnoh) | — |

Dex numbers as of the full sheet-sync pass (`data/RegionalDex.c`, 366 entries) — re-`grep` if the
dex is renumbered again before this route's table is finalized.

## Notes

- **Resolved — Rattata → Shinx:** Rattata (dex-less, `keep=No` in the curation sheet) has been
  replaced by Shinx in all 4 of its night slots (2, 4, 7, 8), keeping the same slot weights
  (20/10/5/5%) and levels. Shinx was chosen over Morpeko (the other Electric option considered) on
  a balance basis — Shinx's BST (263) and catch rate (235) are near-identical to Rattata/Pidgey's,
  while Morpeko (BST 436, no evolution) would be a real power outlier at this frequency on a
  level 2–4 route. This closes the Electric-coverage gap flagged for Falkner's type-coverage audit
  (see the Dark Cave entrance doc's Notes) — Route 30 now offers a wild-caught Electric option
  before the gym, alongside Rock from the Dark Cave entrance.
- **Poliwag/Poliwhirl were part of the dex-sync fix** — before that fix they'd have shown up here
  as another false "cut" mismatch. They're legitimately kept (`keep=Yes` in the sheet) and are now
  correctly in `data/RegionalDex.c` (#346/#347). No action needed on this route's surf table.
- Hoenn/Sinnoh rustling-grass picks (Whismur/Linoone/Buizel/Bidoof) are all dex-less — consistent
  with them not being native Johto/Kanto species; that's likely intentional (they're a special
  "nod to other regions" encounter, separate from regular dex tracking) rather than a curation
  oversight, but worth confirming if the audit ever gets to non-native rustling-grass species as a
  category.
