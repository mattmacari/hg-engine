# Lake of Rage

See `documentation/areas/README.md` for what this doc format is and how to reproduce it for other
areas.

## Header facts

- **ENCDATA constant:** `ENCDATA_T29_LAKE_OF_RAGE` (`data/Encounters.c:5809`)
- **Map constant:** `MAP_T29` (`include/constants/maps.h:92`)
- **Connects:** Route 43 (south). Water only — the red Gyarados is a scripted static encounter, not
  part of this table.
- **Leads toward:** Pryce — the Lake of Rage event starts the Rocket Hideout sequence that unlocks
  Mahogany's gym.

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

**Surf (rate 10):** Magikarp (10–20), Magikarp (5–15), Gyarados (10–20), Gyarados (10–20), Gyarados (10–20).
**Old Rod (rate 25):** Magikarp (10), Magikarp (10), Magikarp (10), Magikarp (10), Magikarp (10).
**Good Rod (rate 50):** Magikarp (20), Magikarp (20), Magikarp (20), Gyarados (20), Magikarp (20).
**Super Rod (rate 75):** Magikarp (40), Gyarados (40), Magikarp (40), Magikarp (40), Magikarp (40).

## Rustling grass (Hoenn/Sinnoh sound species)

Not populated — no land tile here.

## Swarm

- `landSwarm = SPECIES_NONE`, `surfSwarm = SPECIES_MAGIKARP`, `nightFish = SPECIES_GYARADOS`, `fishSwarm = SPECIES_MAGIKARP`.
- **Inert:** this map is not in `sSwarmMapLUT` (`src/swarms.c`).

## Species summary

| Species | Type(s) | Regional Dex # | Method | Time |
|---|---|---|---|---|
| Magikarp | Water | 65 | Surf, Fish, Swarm (surf), Swarm (fish) | — |
| Gyarados | Water/Flying | 66 | Surf, Fish, Fish (night) | — |

Dex numbers as of `data/RegionalDex.c` with 369 entries (Tauros added as #369 in the Jasmine-corridor pass) —
re-`grep` if the dex is renumbered.

## Notes

- Already clean — Magikarp/Gyarados only, both dex-tracked. Canon-correct for the lake, no changes made.
