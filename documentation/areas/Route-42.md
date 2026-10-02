# Route 42

See `documentation/areas/README.md` for what this doc format is and how to reproduce it for other
areas.

## Header facts

- **ENCDATA constant:** `ENCDATA_R42_ROUTE_42` (`data/Encounters.c:5209`)
- **Map constant:** `MAP_R42` (`include/constants/maps.h:48`)
- **Connects:** Ecruteak City (west) ↔ Mahogany Town (east). Mt. Mortar's entrances open off it,
  and parts of the route are split by water.
- **Leads toward:** Pryce (Mahogany Town) — first leg of the approach.
- **Biome Map tie-in:** `HACK_PLAN.md`'s Pryce row needs Fire/Fighting/Rock/Steel counters. Mankey
  here covers Fighting directly.

## Encounter methods active

| Method | Rate | Active? |
|---|---|---|
| Walk | 25 | Yes |
| Surf | 10 | Yes |
| Rock Smash | 0 | No |
| Old Rod | 25 | Yes |
| Good Rod | 50 | Yes |
| Super Rod | 75 | Yes |

## Land encounter table (walk, rate 25)

| Slot | % | Level | Morning | Day | Night |
|---|---|---|---|---|---|
| 1 | 20 | 15 | Mankey | Mankey | Mankey |
| 2 | 20 | 13 | Mareep | Mareep | Mareep |
| 3 | 10 | 15 | Mankey | Mankey | Mankey |
| 4 | 10 | 13 | Mareep | Mareep | Mareep |
| 5 | 10 | 14 | Taillow | Taillow | Woobat |
| 6 | 10 | 14 | Taillow | Taillow | Woobat |
| 7 | 5 | 16 | Taillow | Taillow | Woobat |
| 8 | 5 | 16 | Taillow | Taillow | Woobat |
| 9 | 4 | 15 | Flaaffy | Flaaffy | Flaaffy |
| 10 | 4 | 17 | Flaaffy | Flaaffy | Flaaffy |
| 11 | 1 | 15 | Flaaffy | Flaaffy | Flaaffy |
| 12 | 1 | 17 | Flaaffy | Flaaffy | Flaaffy |

## Water/rod tables

**Surf (rate 10):** Marill (15–25), Surskit (10–20), Azumarill (15–25), Masquerain (15–25), Azumarill (15–25).
**Old Rod (rate 25):** Magikarp (10), Magikarp (10), Magikarp (10), Marill (10), Surskit (10).
**Good Rod (rate 50):** Magikarp (20), Marill (20), Surskit (20), Marill (20), Surskit (20).
**Super Rod (rate 75):** Marill (40), Surskit (40), Magikarp (40), Azumarill (40), Magikarp (40).

## Rustling grass (Hoenn/Sinnoh sound species)

| Region | Slot 1 | Slot 2 |
|---|---|---|
| Hoenn | Whismur | Linoone |
| Sinnoh | Buizel | Bidoof |

## Swarm

- `landSwarm = SPECIES_MANKEY`, `surfSwarm = SPECIES_SURSKIT`, `nightFish = SPECIES_MARILL`, `fishSwarm = SPECIES_MAGIKARP`.
- **Inert:** this map is not in `sSwarmMapLUT` (`src/swarms.c`).

## Species summary

| Species | Type(s) | Regional Dex # | Method | Time |
|---|---|---|---|---|
| Mareep | Electric | 46 | Walk | Morning/Day/Night |
| Flaaffy | Electric | 47 | Walk | Morning/Day/Night |
| Magikarp | Water | 65 | Fish, Swarm (fish) | — |
| Marill | Water/Fairy | 102 | Surf, Fish, Fish (night) | — |
| Azumarill | Water/Fairy | 103 | Surf, Fish | — |
| Mankey | Fighting | 104 | Walk, Swarm (land) | Morning/Day/Night |
| Taillow | Normal/Flying | 207 | Walk | Morning/Day |
| Surskit | Bug/Water | 211 | Surf, Fish, Swarm (surf) | — |
| Masquerain | Bug/Flying | 212 | Surf | — |
| Woobat | Psychic/Flying | 276 | Walk | Night |
| Bidoof | Normal | **not in dex** | Rustling grass (Sinnoh) | — |
| Buizel | Water | **not in dex** | Rustling grass (Sinnoh) | — |
| Linoone | Normal | **not in dex** | Rustling grass (Hoenn) | — |
| Whismur | Normal | **not in dex** | Rustling grass (Hoenn) | — |

Dex numbers as of `data/RegionalDex.c` with 369 entries (Tauros added as #369 in the Jasmine-corridor pass) —
re-`grep` if the dex is renumbered.

## Notes

- **Resolved — Spearow (slots 5–8 morning/day, 30%) → Taillow** (#207, dex-tracked but previously
  spawned nowhere). A straight bird-for-bird swap.
- **Resolved — Zubat (slots 5–8 at night, 30%) → Woobat**, the same bat stand-in used on Route 36
  and in Cliff Cave and Mt. Mortar.
- **Resolved — Goldeen/Seaking replaced** with a mixed freshwater pool shared with Mt. Mortar:
  - **Marill** takes the common slots and **Surskit** the second tier.
  - **Azumarill** and **Masquerain** fill the rare evolved slots.
  - Surf swarm → Surskit; night fish → Marill.
  - Marill was already Mt. Mortar's own species. Surskit/Masquerain were dex-tracked but spawned
    nowhere.
  - Feebas is deliberately **not** on Route 42 — it's kept as a Mt. Mortar-only find (see
    Mt-Mortar.md).
- **Left as-is:** dex-less rustling-grass species (post-game only).
