# Route 35

See `documentation/areas/README.md` for what this doc format is and how to reproduce it for other
areas.

## Header facts

- **ENCDATA constant:** `ENCDATA_R35_ROUTE_35` (`data/Encounters.c:2209`)
- **Map constant:** `MAP_R35` (`include/constants/maps.h:43`)
- **Connects:** Goldenrod City (south) ↔ National Park (north).
- **Leads toward:** Morty (Ecruteak City) — this is the first leg of the Goldenrod→Ecruteak
  corridor (Route 35 → National Park → Route 36 → Ecruteak).
- **Biome Map tie-in:** `HACK_PLAN.md`'s Morty row counter-access note: "Dark needed (Ghost's
  other weakness besides Ghost itself)." No Dark-type appears on this route — see Route-36.md for
  where that gap actually gets closed (last route before the gym).

## Encounter methods active

| Method | Rate | Active? |
|---|---|---|
| Walk | 25 | Yes |
| Surf | 15 | Yes |
| Rock Smash | 0 | No |
| Old Rod | 25 | Yes |
| Good Rod | 50 | Yes |
| Super Rod | 75 | Yes |

## Land encounter table (walk, rate 25)

| Slot | % | Level | Morning | Day | Night |
|---|---|---|---|---|---|
| 1 | 20 | 12 | Shroomish | Shroomish | Shroomish |
| 2 | 20 | 12 | Slakoth | Slakoth | Slakoth |
| 3 | 10 | 12 | Shroomish | Shroomish | Shroomish |
| 4 | 10 | 12 | Slakoth | Slakoth | Slakoth |
| 5 | 10 | 14 | Wynaut | Wynaut | Wynaut |
| 6 | 10 | 14 | Wynaut | Wynaut | Wynaut |
| 7 | 5 | 10 | Abra | Abra | Abra |
| 8 | 5 | 10 | Abra | Abra | Abra |
| 9 | 4 | 14 | Pidgey | Pidgey | Hoothoot |
| 10 | 4 | 10 | Ditto | Ditto | Ditto |
| 11 | 1 | 14 | Pidgey | Pidgey | Hoothoot |
| 12 | 1 | 12 | Yanma | Yanma | Yanma |

## Water/rod tables

**Surf (rate 15):** Psyduck ×2 (15/10%), Golduck ×3 (15/15/31%, all level 25–31).
**Old Rod (10/10/10/10/10):** Magikarp ×3, Poliwag ×2 (all level 10).
**Good Rod (20/20/20/20/20):** Magikarp, Poliwag ×4 (all level 20).
**Super Rod (40/40/40/40/40):** Poliwag ×3, Magikarp ×2 (all level 40).

## Rustling grass (Hoenn/Sinnoh sound species)

| Region | Slot 1 | Slot 2 |
|---|---|---|
| Hoenn | Whismur | Linoone |
| Sinnoh | Buizel | Bidoof |

## Swarm

- `landSwarm = SPECIES_YANMA`, `surfSwarm = SPECIES_PSYDUCK`, `nightFish = SPECIES_POLIWAG`,
  `fishSwarm = SPECIES_MAGIKARP`.
- **Active:** `MAP_R35` **is** in `sSwarmMapLUT` (`src/swarms.c:24`, `SWARM_GRASS`) — the Yanma
  land-swarm event actually functions here.

## Species summary

| Species | Type(s) | Regional Dex # | Method | Time |
|---|---|---|---|---|
| Pidgey | Normal/Flying | 10 | Walk | Morning/Day |
| Hoothoot | Normal/Flying | 13 | Walk | Night |
| Ditto | Normal | 75 | Walk | Morning/Day/Night |
| Yanma | Bug/Flying | 78 | Walk, Swarm (land, active) | Morning/Day/Night |
| Abra | Psychic | 72 | Walk | Morning/Day/Night |
| Shroomish | Grass | 213 | Walk | Morning/Day/Night |
| Slakoth | Normal | 215 | Walk | Morning/Day/Night |
| Wynaut | Psychic | 229 | Walk | Morning/Day/Night |
| Psyduck | Water | **not in regional dex** | Surf | — |
| Golduck | Water | **not in regional dex** | Surf | — |
| Poliwag | Water | 346 | Fish | — |
| Magikarp | Water | 65 | Fish, Swarm (fish, inert) | — |
| Whismur | Normal | **not in regional dex** | Rustling grass (Hoenn) | — |
| Linoone | Normal | **not in regional dex** | Rustling grass (Hoenn) | — |
| Buizel | Water | **not in regional dex** | Rustling grass (Sinnoh) | — |
| Bidoof | Normal | **not in regional dex** | Rustling grass (Sinnoh) | — |

Dex numbers as of the full sheet-sync pass (`data/RegionalDex.c`, 368 entries) — re-`grep` if the
dex is renumbered again before this route's table is finalized.

## Notes

- **Resolved — Nidoran♂/♀ and Drowzee replaced (80% of the land table).** These three sat
  dex-less and made up the bulk of the table — bigger than Route 34's Drowzee problem (50%) that
  already got the same treatment. Replaced with **Shroomish**, **Slakoth**, and **Wynaut**, all
  three already regional-dex-tracked (#213/#215/#229) and not spawning anywhere else in the build
  at the time of the swap. Shroomish previews the forest biome of National Park (next area north);
  Slakoth fills the "common everyday critter" filler role Nidoran had; Wynaut keeps this route's
  existing Psychic thread (alongside Abra) and ties into Wobbuffet's separate shaking-grass rare
  encounter elsewhere in the game.
- Psyduck/Golduck (Surf) and the Hoenn/Sinnoh rustling-grass species (Whismur/Linoone,
  Buizel/Bidoof) are still dex-less — left as-is. No Gen3+ Water-type alternative for the surf
  slot is currently `keep = Yes` in `data/RegionalDex.c` in this build's curation, and the
  rustling-grass fillers are the same routine `keep = No` cut seen throughout the rest of the game
  (see National Park's Cherubi for the same category), per
  [[feedback_dex_encounter_mismatches]]. Revisit if the regional dex curation itself changes.
- No Dark-type on this route. Not treated as this route's problem to fix — see Route-36.md, the
  last leg before Ecruteak, for where the Morty-row Dark-coverage gap actually gets closed.
- `surfSwarm`/`fishSwarm`/`nightFish` fields are populated but `SWARM_SURF`/fish swarm categories
  aren't checked against `sSwarmMapLUT` the same way `SWARM_GRASS` is for this route — only the
  land swarm (Yanma) is confirmed active here.
