# Ecruteak City

See `documentation/areas/README.md` for what this doc format is and how to reproduce it for other
areas.

## Header facts

- **ENCDATA constant:** `ENCDATA_T27_ECRUTEAK_CITY` (`data/Encounters.c:2709`)
- **Map constant:** `MAP_T27` (`include/constants/maps.h:82`)
- **Connects:** Route 36 (south, the approach corridor) and Route 38 (east, leads onward toward
  Olivine — post-Morty progression, not relevant here).
- **Leads toward:** Morty — this is the gym's own city. No land walk encounters (city tile), only
  water/fishing on the lake plus headbutt trees.
- **Biome Map tie-in:** `HACK_PLAN.md`'s Morty row calls Burned Tower/old-town lore "already a
  strong ghost biome, no change needed" — that's about the gym's own trainers/flavor, not a claim
  that wild Ghost-type encounters exist in the city or its water. None do, and none are needed;
  Morty's Ghost identity comes from his roster (`data/Trainers.c`), not the surrounding wild table.

## Encounter methods active

| Method | Rate | Active? |
|---|---|---|
| Walk | 0 | No (city tile, no grass) |
| Surf | 15 | Yes |
| Rock Smash | 0 | No |
| Old Rod | 25 | Yes |
| Good Rod | 50 | Yes |
| Super Rod | 75 | Yes |

## Water/rod tables

**Surf (rate 15):** Poliwag ×2 (15/10%), Poliwhirl ×3 (15/15/15%).
**Old Rod (10/10/10/10/10):** Magikarp ×3, Poliwag ×2 (all level 10).
**Good Rod (20/20/20/20/20):** Magikarp, Poliwag ×4 (all level 20).
**Super Rod (40/40/40/40/40):** Poliwag ×3, Magikarp ×2 (all level 40).

Identical rod tables to Route 35's — this whole lake system shares one fishing pool.

## Swarm

- `surfSwarm = SPECIES_POLIWAG`, `nightFish = SPECIES_POLIWAG`, `fishSwarm = SPECIES_MAGIKARP`.
  `landSwarm = SPECIES_NONE` (no grass tile to swarm on).
- `MAP_T27` is not in `sSwarmMapLUT` (`src/swarms.c`) — moot anyway since there's no land swarm
  species set.

## Headbutt trees (`data/Headbutt.c`, `.ecruteakCity`)

Same species set as National Park's trees (18 normal-tier trees, no special tier here).

| Species | Type(s) | Regional Dex # | Level |
|---|---|---|---|
| Hoothoot | Normal/Flying | 13 | 12–17 |
| Pineco | Bug | 76 | 12–14 |
| Exeggcute | Grass/Psychic | 82 | 12–17 |
| Spinarak | Bug/Poison | 28 | 15–17 |

## Species summary

| Species | Type(s) | Regional Dex # | Method | Time |
|---|---|---|---|---|
| Hoothoot | Normal/Flying | 13 | Headbutt | — |
| Pineco | Bug | 76 | Headbutt | — |
| Spinarak | Bug/Poison | 28 | Headbutt | — |
| Exeggcute | Grass/Psychic | 82 | Headbutt | — |
| Poliwag | Water | 346 | Surf, Fish | — |
| Poliwhirl | Water | 347 | Surf | — |
| Magikarp | Water | 65 | Fish, Swarm (fish) | — |

Dex numbers as of the full sheet-sync pass (`data/RegionalDex.c`, 368 entries) — re-`grep` if the
dex is renumbered again before this area's table is finalized.

## Notes

- No dex/encounter mismatches — every species here is already regional-dex-tracked. No curation
  or encounter changes made in this city.
- No Dark-type here and none needed — that gap was already closed on Route 36, the approach route
  immediately before this city (see Route-36.md).
- Purely a water/headbutt location as far as wild encounters go; the gym itself (indoor, no wild
  table) is where Morty's actual Ghost-type identity lives.
