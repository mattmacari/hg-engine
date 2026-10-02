# Blackthorn City

See `documentation/areas/README.md` for what this doc format is and how to reproduce it for other
areas.

## Header facts

- **ENCDATA constant:** `ENCDATA_T30_BLACKTHORN_CITY` (`data/Encounters.c:6509`)
- **Map constant:** `MAP_T30` (`include/constants/maps.h:93`)
- **Connects:** Ice Path (west), Route 45 (south), and Dragon's Den (behind the gym, by water).
- **Leads toward:** Clair — the gym's own city. Water/fishing only.

## Encounter methods active

| Method | Rate | Active? |
|---|---|---|
| Walk | 0 | No |
| Surf | 10 | Yes |
| Rock Smash | 0 | No |
| Old Rod | 25 | Yes |
| Good Rod | 50 | Yes |
| Super Rod | 75 | Yes |

## Water/rod tables

**Surf (rate 10):** Magikarp (10–20), Magikarp (5–15), Magikarp (2–10), Magikarp (2–10), Magikarp (2–10).
**Old Rod (rate 25):** Magikarp (10), Magikarp (10), Magikarp (10), Poliwag (10), Poliwag (10).
**Good Rod (rate 50):** Magikarp (20), Poliwag (20), Poliwag (20), Poliwag (20), Poliwag (20).
**Super Rod (rate 75):** Poliwag (40), Poliwag (40), Magikarp (40), Poliwag (40), Magikarp (40).

## Rustling grass (Hoenn/Sinnoh sound species)

Not populated — no land tile here.

## Swarm

- `landSwarm = SPECIES_NONE`, `surfSwarm = SPECIES_MAGIKARP`, `nightFish = SPECIES_POLIWAG`, `fishSwarm = SPECIES_MAGIKARP`.
- **Inert:** this map is not in `sSwarmMapLUT` (`src/swarms.c`).

## Species summary

| Species | Type(s) | Regional Dex # | Method | Time |
|---|---|---|---|---|
| Magikarp | Water | 65 | Surf, Fish, Swarm (surf), Swarm (fish) | — |
| Poliwag | Water | 346 | Fish, Fish (night) | — |

Dex numbers as of `data/RegionalDex.c` with 374 entries (Horsea/Seadra/Kingdra/Swablu/Altaria added as #370–374 in the Clair pass) —
re-`grep` if the dex is renumbered.

## Notes

- Already clean — Magikarp/Poliwag only, both dex-tracked. No changes made.
