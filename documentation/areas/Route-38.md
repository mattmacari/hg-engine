# Route 38

See `documentation/areas/README.md` for what this doc format is and how to reproduce it for other
areas.

## Header facts

- **ENCDATA constant:** `ENCDATA_R38_ROUTE_38` (`data/Encounters.c:3809`)
- **Map constant:** `MAP_R38` (`include/constants/maps.h:46`)
- **Connects:** Ecruteak City (east) ↔ Route 39 (west/south). Moomoo Farm sits at the Route 38/39
  bend.
- **Leads toward:** Jasmine (Olivine City) — first leg of the Ecruteak → Olivine walk. The player
  passes through here before Surfing to Cianwood, so it also counts toward Chuck's counter-access
  (Snubbull, see Cianwood-City.md).
- **Biome Map tie-in:** `HACK_PLAN.md`'s Jasmine row: Steel weak to Fire/Fighting/Ground; Electric
  partner fits "lighthouse/generator flavor". This route is pastoral ranch land (Moomoo Farm), so
  the rework leans livestock + Electric rather than industrial.

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
| 2 | 20 | 16 | Flaaffy | Flaaffy | Flaaffy |
| 3 | 10 | 16 | Ponyta | Ponyta | Ponyta |
| 4 | 10 | 16 | Flaaffy | Flaaffy | Flaaffy |
| 5 | 10 | 16 | Magnemite | Magnemite | Magnemite |
| 6 | 10 | 16 | Magnemite | Magnemite | Magnemite |
| 7 | 5 | 16 | Farfetch’d | Farfetch’d | Hoothoot |
| 8 | 5 | 16 | Farfetch’d | Farfetch’d | Hoothoot |
| 9 | 4 | 13 | Miltank | Miltank | Miltank |
| 10 | 4 | 13 | Tauros | Tauros | Tauros |
| 11 | 1 | 13 | Miltank | Miltank | Miltank |
| 12 | 1 | 13 | Snubbull | Snubbull | Snubbull |

## Rustling grass (Hoenn/Sinnoh sound species)

| Region | Slot 1 | Slot 2 |
|---|---|---|
| Hoenn | Plusle | Minun |
| Sinnoh | Shinx | Shinx |

## Swarm

- `landSwarm = SPECIES_SNUBBULL`, `surfSwarm = SPECIES_NONE`, `nightFish = SPECIES_NONE`, `fishSwarm = SPECIES_NONE`.
- **Active:** `MAP_R38` is in `sSwarmMapLUT` (`src/swarms.c:25`, `SWARM_GRASS`) — the Snubbull land swarm actually fires here.

## Species summary

| Species | Type(s) | Regional Dex # | Method | Time |
|---|---|---|---|---|
| Hoothoot | Normal/Flying | 13 | Walk | Night |
| Flaaffy | Electric | 47 | Walk | Morning/Day/Night |
| Magnemite | Electric/Steel | 91 | Walk | Morning/Day/Night |
| Snubbull | Fairy | 95 | Walk, Swarm (land) | Morning/Day/Night |
| Miltank | Normal | 112 | Walk | Morning/Day/Night |
| Farfetch’d | Normal/Flying | 120 | Walk | Morning/Day |
| Ponyta | Fire | 157 | Walk | Morning/Day/Night |
| Plusle | Electric | 219 | Rustling grass (Hoenn) | — |
| Minun | Electric | 220 | Rustling grass (Hoenn) | — |
| Shinx | Electric | 235 | Rustling grass (Sinnoh) | — |
| Tauros | Normal | 369 | Walk | Morning/Day/Night |

Dex numbers as of `data/RegionalDex.c` with 369 entries (Tauros added as #369 in this pass) —
re-`grep` if the dex is renumbered.

## Notes

- **Resolved — Rattata/Raticate replaced (60% of day encounters, 70% at night).** Both were dex-cut.
  Slots 1/3 (Rattata) → **Ponyta**, slots 2/4 (Raticate) → **Flaaffy**, night slots 7/8 (Rattata)
  → **Hoothoot** (matches Route 37's night table). Ponyta is a ranch horse that fits Moomoo Farm and
  adds a second Fire option for Jasmine; it was dex-tracked (#157) but only spawned in Kanto/Mt.
  Silver. Flaaffy continues Route 32's Mareep and fits the Electric half of Jasmine's
  double-battle pairing.
- **Resolved — Tauros added to the regional dex (#369)** rather than replaced. It's Miltank's
  canon Moomoo Farm partner, and it also spawns on Routes 39/47/48. The curation sheet export
  (`data/generated/species_dex_meta.csv`) was flipped to `keep = Yes` alongside.
- Snubbull (slot 12, 1%, plus the active land swarm) is the Fairy foothold that Chuck's
  counter-access relies on — left untouched.
