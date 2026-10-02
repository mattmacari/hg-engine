# New Bark Town

See `documentation/areas/README.md` for what this doc format is and how to reproduce it for other
areas.

## Header facts

- **ENCDATA constant:** `ENCDATA_T20_NEW_BARK_TOWN` (`data/Encounters.c:9`)
- **Map constant:** `MAP_T20` (`include/constants/maps.h:64`)
- **Connects:** Route 29 (west), Route 27 (east, by Surf, toward Kanto).
- **Leads toward:** starting town. Water/fishing only, reachable once the player has Surf or a rod.

## Encounter methods active

| Method | Rate | Active? |
|---|---|---|
| Walk | 0 | No |
| Surf | 15 | Yes |
| Rock Smash | 0 | No |
| Old Rod | 25 | Yes |
| Good Rod | 50 | Yes |
| Super Rod | 75 | Yes |

## Water/rod tables

**Surf (rate 15):** Chinchou (15–25), Chinchou (10–20), Lanturn (15–25), Lanturn (15–25), Lanturn (15–25).
**Old Rod (rate 25):** Magikarp (10), Magikarp (10), Magikarp (10), Chinchou (10), Chinchou (10).
**Good Rod (rate 50):** Magikarp (20), Chinchou (20), Chinchou (20), Shellder (20), Chinchou (20).
**Super Rod (rate 75):** Chinchou (40), Shellder (40), Lanturn (40), Lanturn (40), Lanturn (40).

## Rustling grass (Hoenn/Sinnoh sound species)

Not populated — no land tile here.

## Swarm

- `landSwarm = SPECIES_NONE`, `surfSwarm = SPECIES_CHINCHOU`, `nightFish = SPECIES_SHELLDER`, `fishSwarm = SPECIES_MAGIKARP`.
- **Inert:** this map is not in `sSwarmMapLUT` (`src/swarms.c`).

## Species summary

| Species | Type(s) | Regional Dex # | Method | Time |
|---|---|---|---|---|
| Magikarp | Water | 65 | Fish, Swarm (fish) | — |
| Shellder | Water | 127 | Fish, Fish (night) | — |
| Chinchou | Water/Electric | 132 | Surf, Fish, Swarm (surf) | — |
| Lanturn | Water/Electric | 133 | Surf, Fish | — |

Dex numbers as of `data/RegionalDex.c` with 377 entries —
re-`grep` if the dex is renumbered.

## Notes

- **Resolved — early-game cleanup pass (after the Clair pass).** Tentacool/Tentacruel →
  **Chinchou/Lanturn** on surf, the rods and the surf swarm. This deepens the town's existing
  Chinchou/Shellder pool, the same approach as Route 47, instead of importing Staryu.
