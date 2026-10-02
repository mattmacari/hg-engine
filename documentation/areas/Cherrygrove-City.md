# Cherrygrove City

See `documentation/areas/README.md` for what this doc format is and how to reproduce it for other
areas.

## Header facts

- **ENCDATA constant:** `ENCDATA_T21_CHERRYGROVE_CITY` (`data/Encounters.c:209`)
- **Map constant:** `MAP_T21` (`include/constants/maps.h:71`)
- **Connects:** Route 29 (east), Route 30 (north).
- **Leads toward:** Falkner. Water/fishing only.

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

**Surf (rate 15):** Staryu (15–25), Staryu (10–20), Starmie (15–25), Starmie (15–25), Starmie (15–25).
**Old Rod (rate 25):** Magikarp (10), Magikarp (10), Magikarp (10), Shellder (10), Shellder (10).
**Good Rod (rate 50):** Magikarp (20), Shellder (20), Shellder (20), Corsola (20), Shellder (20).
**Super Rod (rate 75):** Shellder (40), Corsola (40), Shellder (40), Cloyster (40), Shellder (40).

## Rustling grass (Hoenn/Sinnoh sound species)

Not populated — no land tile here.

## Swarm

- `landSwarm = SPECIES_NONE`, `surfSwarm = SPECIES_STARYU`, `nightFish = SPECIES_STARYU`, `fishSwarm = SPECIES_MAGIKARP`.
- **Inert:** this map is not in `sSwarmMapLUT` (`src/swarms.c`).

## Species summary

| Species | Type(s) | Regional Dex # | Method | Time |
|---|---|---|---|---|
| Magikarp | Water | 65 | Fish, Swarm (fish) | — |
| Staryu | Water | 125 | Surf, Swarm (surf), Fish (night) | — |
| Starmie | Water/Psychic | 126 | Surf | — |
| Shellder | Water | 127 | Fish | — |
| Cloyster | Water/Ice | 128 | Fish | — |
| Corsola | Water/Rock | 129 | Fish | — |

Dex numbers as of `data/RegionalDex.c` with 377 entries —
re-`grep` if the dex is renumbered.

## Notes

- **Resolved — early-game cleanup pass (after the Clair pass).** Tentacool/Tentacruel →
  **Staryu/Starmie** and Krabby/Kingler → **Shellder/Cloyster** (the Route 40/41/Cianwood
  mapping). Corsola and the night-fish Staryu are unchanged.
