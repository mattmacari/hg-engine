# Olivine City

See `documentation/areas/README.md` for what this doc format is and how to reproduce it for other
areas.

## Header facts

- **ENCDATA constant:** `ENCDATA_T26_OLIVINE_CITY` (`data/Encounters.c:4009`)
- **Map constant:** `MAP_T26` (`include/constants/maps.h:81`)
- **Connects:** Route 39 (north), Route 40 (west, Surf → Cianwood).
- **Leads toward:** Jasmine — this is the gym's own city. The player reaches it before Chuck but
  fights Jasmine after returning from Cianwood with the medicine. Olivine Lighthouse has **no wild
  encounter table** (no `ENCDATA_*` entry), so it needs no area doc.
- **Biome Map tie-in:** "Olivine's port/lighthouse industrial setting fits Steel ecology well
  already." The wild data here is only water, which continues the Route 40/41/Cianwood marine pool.

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

Dex numbers as of `data/RegionalDex.c` with 369 entries (Tauros added as #369 in this pass) —
re-`grep` if the dex is renumbered.

## Notes

- **Resolved — Tentacool/Tentacruel/Krabby/Kingler replaced**, using the same mapping as Route
  40/41/Cianwood (see Route-40.md): Tentacool → **Staryu**, Tentacruel → **Starmie**, Krabby →
  **Shellder**, Kingler → **Cloyster**. `surfSwarm` (Tentacool) → Staryu too. The surf/rod tables
  now match Cianwood's exactly, so the whole Olivine → Cianwood sea is one pool.
