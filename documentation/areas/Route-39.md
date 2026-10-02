# Route 39

See `documentation/areas/README.md` for what this doc format is and how to reproduce it for other
areas.

## Header facts

- **ENCDATA constant:** `ENCDATA_R39_ROUTE_39` (`data/Encounters.c:3909`)
- **Map constant:** `MAP_R39` (`include/constants/maps.h:47`)
- **Connects:** Route 38 / Moomoo Farm (north) ↔ Olivine City (south).
- **Leads toward:** Jasmine (Olivine City) — last route before Olivine.
- **Biome Map tie-in:** same as Route 38 — pastoral ranch land on the way into the port city.

## Encounter methods active

| Method | Rate | Active? |
|---|---|---|
| Walk | 25 | Yes |
| Surf | 0 | No |
| Rock Smash | 0 | No |
| Old Rod | 0 | No |
| Good Rod | 0 | No |
| Super Rod | 0 | No |

## Land encounter table (walk, rate 25)

| Slot | % | Level | Morning | Day | Night |
|---|---|---|---|---|---|
| 1 | 20 | 16 | Ponyta | Ponyta | Ponyta |
| 2 | 20 | 17 | Flaaffy | Flaaffy | Flaaffy |
| 3 | 10 | 16 | Ponyta | Ponyta | Ponyta |
| 4 | 10 | 17 | Flaaffy | Flaaffy | Flaaffy |
| 5 | 10 | 16 | Magnemite | Magnemite | Magnemite |
| 6 | 10 | 16 | Magnemite | Magnemite | Magnemite |
| 7 | 5 | 16 | Farfetch’d | Farfetch’d | Hoothoot |
| 8 | 5 | 16 | Farfetch’d | Farfetch’d | Hoothoot |
| 9 | 4 | 15 | Miltank | Miltank | Miltank |
| 10 | 4 | 15 | Tauros | Tauros | Tauros |
| 11 | 1 | 15 | Miltank | Miltank | Miltank |
| 12 | 1 | 15 | Tauros | Tauros | Tauros |

## Rustling grass (Hoenn/Sinnoh sound species)

| Region | Slot 1 | Slot 2 |
|---|---|---|
| Hoenn | Plusle | Minun |
| Sinnoh | Shinx | Shinx |

## Swarm

- `landSwarm = SPECIES_PONYTA`, `surfSwarm = SPECIES_NONE`, `nightFish = SPECIES_NONE`, `fishSwarm = SPECIES_NONE`.
- **Inert:** this map is not in `sSwarmMapLUT` (`src/swarms.c`).

## Species summary

| Species | Type(s) | Regional Dex # | Method | Time |
|---|---|---|---|---|
| Hoothoot | Normal/Flying | 13 | Walk | Night |
| Flaaffy | Electric | 47 | Walk | Morning/Day/Night |
| Magnemite | Electric/Steel | 91 | Walk | Morning/Day/Night |
| Miltank | Normal | 112 | Walk | Morning/Day/Night |
| Farfetch’d | Normal/Flying | 120 | Walk | Morning/Day |
| Ponyta | Fire | 157 | Walk, Swarm (land) | Morning/Day/Night |
| Plusle | Electric | 219 | Rustling grass (Hoenn) | — |
| Minun | Electric | 220 | Rustling grass (Hoenn) | — |
| Shinx | Electric | 235 | Rustling grass (Sinnoh) | — |
| Tauros | Normal | 369 | Walk | Morning/Day/Night |

Dex numbers as of `data/RegionalDex.c` with 369 entries (Tauros added as #369 in this pass) —
re-`grep` if the dex is renumbered.

## Notes

- **Resolved — Rattata/Raticate replaced**, identical to Route 38: Rattata → **Ponyta**, Raticate
  → **Flaaffy**, night-only Rattata (slots 7/8) → **Hoothoot**. The land swarm was also Rattata;
  changed to **Ponyta** for tidiness (it's inert — `MAP_R39` isn't in the swarm LUT).
- Tauros (slots 10/12, 5%) stays — now dex-tracked as #369 (see Route-38.md).
