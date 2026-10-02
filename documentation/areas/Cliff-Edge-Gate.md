# Cliff Edge Gate

See `documentation/areas/README.md` for what this doc format is and how to reproduce it for other
areas.

## Header facts

- **ENCDATA constant:** `ENCDATA_D48R0101_CLIFF_EDGE_GATE` (`data/Encounters.c:8209`)
- **Map constant:** `MAP_D48R0101` (`include/constants/maps.h:283`)
- **Connects:** Cianwood City (east) ↔ Route 47 (west).
- **Leads toward:** Optional side area, off the critical path. It is reachable from Cianwood City via Cliff Edge Gate,
  which puts it in the Chuck → Jasmine window.

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

**Surf (rate 15):** Wooper (20–30), Wooper (20–30), Quagsire (30–40), Quagsire (30–40), Quagsire (30–40).
**Old Rod (rate 25):** Magikarp (10), Magikarp (10), Magikarp (10), Magikarp (10), Magikarp (10).
**Good Rod (rate 50):** Magikarp (20), Magikarp (20), Magikarp (20), Poliwag (20), Poliwag (20).
**Super Rod (rate 75):** Magikarp (40), Magikarp (40), Poliwag (40), Poliwag (40), Poliwag (40).

## Rustling grass (Hoenn/Sinnoh sound species)

Not populated — no land tile here.

## Swarm

- `landSwarm = SPECIES_NONE`, `surfSwarm = SPECIES_WOOPER`, `nightFish = SPECIES_MAGIKARP`, `fishSwarm = SPECIES_MAGIKARP`.
- **Inert:** this map is not in `sSwarmMapLUT` (`src/swarms.c`).

## Species summary

| Species | Type(s) | Regional Dex # | Method | Time |
|---|---|---|---|---|
| Wooper | Water/Ground | 49 | Surf, Swarm (surf) | — |
| Quagsire | Water/Ground | 50 | Surf | — |
| Magikarp | Water | 65 | Fish, Fish (night), Swarm (fish) | — |
| Poliwag | Water | 346 | Fish | — |

Dex numbers as of `data/RegionalDex.c` with 369 entries (Tauros added as #369 in this pass) —
re-`grep` if the dex is renumbered.

## Notes

- Already clean — every species is dex-tracked. No changes made.
