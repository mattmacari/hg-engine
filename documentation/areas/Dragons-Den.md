# Dragon's Den

See `documentation/areas/README.md` for what this doc format is and how to reproduce it for other
areas.

## Header facts

- **ENCDATA constant:** `ENCDATA_D44R0102_DRAGONS_DEN` (`data/Encounters.c:6609`)
- **Map constant:** `MAP_D44R0102` (`include/constants/maps.h:257`)
- **Connects:** Blackthorn City (Surf, behind the gym).
- **Leads toward:** Clair — the story sends the player here after her gym battle. Water only. The
  elder's gift Dratini (with Extreme Speed, if you answer his quiz correctly) is scripted, not part
  of this table.

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

**Surf (rate 10):** Magikarp (10–20), Magikarp (5–15), Dratini (5–15), Dratini (5–15), Dratini (5–15).
**Old Rod (rate 25):** Magikarp (10), Magikarp (10), Magikarp (10), Magikarp (10), Magikarp (10).
**Good Rod (rate 50):** Magikarp (20), Magikarp (20), Magikarp (20), Dratini (20), Magikarp (20).
**Super Rod (rate 75):** Magikarp (40), Dratini (40), Magikarp (40), Dragonair (40), Magikarp (40).

## Rustling grass (Hoenn/Sinnoh sound species)

Not populated — no land tile here.

## Swarm

- `landSwarm = SPECIES_NONE`, `surfSwarm = SPECIES_MAGIKARP`, `nightFish = SPECIES_DRATINI`, `fishSwarm = SPECIES_MAGIKARP`.
- **Inert:** this map is not in `sSwarmMapLUT` (`src/swarms.c`).

## Species summary

| Species | Type(s) | Regional Dex # | Method | Time |
|---|---|---|---|---|
| Magikarp | Water | 65 | Surf, Fish, Swarm (surf), Swarm (fish) | — |
| Dratini | Dragon | 189 | Surf, Fish, Fish (night) | — |
| Dragonair | Dragon | 190 | Fish | — |

Dex numbers as of `data/RegionalDex.c` with 374 entries (Horsea/Seadra/Kingdra/Swablu/Altaria added as #370–374 in the Clair pass) —
re-`grep` if the dex is renumbered.

## Notes

- Already clean — Magikarp/Dratini/Dragonair, all dex-tracked and canon-correct. No changes made.
