# Dark Cave (Route 31 Entrance)

See `documentation/areas/README.md` for what this doc format is and how to reproduce it for other
areas.

## Header facts

- **ENCDATA constant:** `ENCDATA_D42R0102_DARK_CAVE_ROUTE_31_ENTRANCE` (`data/Encounters.c:6909`)
- **Map constant:** `MAP_D42R0102` (`include/constants/maps.h:180`)
- **Connects:** Route 31 ↔ deeper Dark Cave (eventually to the Route 45/46 side, via
  `ENCDATA_D42R0101_DARK_CAVE_ROUTE_45_ENTRANCE`, not covered by this doc).
- **Leads toward:** Falkner (Violet City) — optional side-detour off Route 31, not mandatory to
  reach the gym.
- **Biome Map tie-in:** this is the area `HACK_PLAN.md`'s Falkner row explicitly names as the Rock
  counter source: "Rock via Geodude (Dark Cave/Route 31, already vanilla-natural)." Confirmed —
  Geodude is this area's dominant land species.

## Encounter methods active

| Method | Rate | Active? |
|---|---|---|
| Walk | 10 | Yes |
| Surf | 10 | Yes |
| Rock Smash | 50 | Yes (highest rate of any Falkner-approach area) |
| Old Rod | 25 | Yes |
| Good Rod | 50 | Yes |
| Super Rod | 75 | Yes |

Notably lower walk rate (10, vs. 25 on the routes) but a much higher Rock Smash rate — consistent
with a cave interior where wall-cracking is the primary interaction, not grass-walking.

## Land encounter table (walk, rate 10)

Identical across morning/day/night — caves have no time-of-day variation here.

| Slot | % | Level | Species |
|---|---|---|---|
| 1 | 20 | 3 | Geodude |
| 2 | 20 | 2 | Zubat |
| 3 | 10 | 3 | Geodude |
| 4 | 10 | 2 | Zubat |
| 5 | 10 | 2 | Geodude |
| 6 | 10 | 2 | Geodude |
| 7 | 5 | 4 | Geodude |
| 8 | 5 | 4 | Geodude |
| 9 | 4 | 3 | Zubat |
| 10 | 4 | 4 | Zubat |
| 11 | 1 | 3 | Zubat |
| 12 | 1 | 4 | Dunsparce |

## Water/rod tables

**Surf (rate 10):** Magikarp in all 5 slots (60/30/5/4/1%, levels 10–20/5–15/2–10/2–10/2–10) —
a small underground stream, not a real water route.
**Rock Smash (rate 50, 90/10):** Dunsparce (4–8), Geodude (8–14)
**Old Rod (60/30/5/4/1):** Magikarp ×3, Goldeen ×2 (all level 10)
**Good Rod (40/40/15/4/1):** Magikarp, Goldeen ×4 (all level 20)
**Super Rod (40/40/15/4/1):** Goldeen ×2, Magikarp, Seaking, Magikarp (all level 40)

## Rustling grass (Hoenn/Sinnoh sound species)

| Region | Slot 1 | Slot 2 |
|---|---|---|
| Hoenn | Absol | Makuhita |
| Sinnoh | Bronzor | Chingling |

Same mechanic as the outdoor routes despite being a cave interior — "grass" rustling here is a
vanilla quirk of this being the map's registered sound-encounter table, not a literal patch of
grass underground.

## Swarm

- `landSwarm = SPECIES_DUNSPARCE`, `surfSwarm = SPECIES_MAGIKARP`, `fishSwarm = SPECIES_MAGIKARP`,
  `nightFish = SPECIES_GOLDEEN`
- **Active, unlike every other Falkner-approach area documented so far:** `MAP_D42R0102` **is** in
  `sSwarmMapLUT` (`src/swarms.c`, `SWARM_GRASS` type). On the days this map rolls for the swarm,
  wild Geodude/Zubat/Dunsparce encounters here are replaced with a Dunsparce swarm. Worth knowing
  before touching `landSwarm` — it isn't dead weight here.

## Species summary

| Species | Type(s) | Regional Dex # | Method | Time |
|---|---|---|---|---|
| Geodude | Rock/Ground | 30 | Walk/Rock Smash | All |
| Zubat | Poison/Flying | **not in regional dex** | Walk | All |
| Dunsparce | Normal | 45 | Walk/Rock Smash | All |
| Magikarp | Water | 65 | Surf/Fish | — |
| Goldeen | Water | **not in regional dex** | Fish | — |
| Seaking | Water | **not in regional dex** | Fish | — |
| Absol | Dark | 228 | Rustling grass (Hoenn) | — |
| Makuhita | Fighting | **not in regional dex** | Rustling grass (Hoenn) | — |
| Bronzor | Steel/Psychic | **not in regional dex** | Rustling grass (Sinnoh) | — |
| Chingling | Psychic | **not in regional dex** | Rustling grass (Sinnoh) | — |

Dex numbers as of the full sheet-sync pass (`data/RegionalDex.c`, 366 entries) — re-`grep` if the
dex is renumbered again before this area's table is finalized.

## Notes

- **Zubat is dex-less, and this is a resolved evolution-chain question, not an open one:** the
  curation sheet marks `keep=No` for the entire Zubat → Golbat → Crobat line. Before the
  [[dex-curation]] sync fix this session, Crobat was still sitting in `data/RegionalDex.c` despite
  that — a leftover that's now been corrected (Crobat removed). So Zubat staying dex-less here is
  consistent and intentional, not a mismatch needing a swap-in like Route 29's Rattata.
- **Geodude confirms the Biome Map's Falkner counter-access note** — it's genuinely the dominant
  species here (2 of the top-2 slot weights), so the "Rock via Geodude, already vanilla-natural"
  claim in `HACK_PLAN.md` holds up against the actual data.
- Goldeen/Seaking dex-less is consistent with the same pattern on Route 30/31/Cherrygrove
  fishing tables — routine, not a bug (`keep=No` in the sheet).
- **Type-coverage relevance (Pillar 3) — this closes out the Falkner pre-gym audit:** across
  Routes 29/30/31 + this cave, the player has Rock (Geodude, here) and, as of the Cutiefly swap,
  a Fairy-typed mon on Route 29 (not itself an Ice/Electric/Rock counter, but notable for the
  hack's Fairy presence). **Electric is still not covered anywhere on the critical path** — the
  Biome Map's own suggestion ("pull Mareep earlier onto Route 32's farmland edge") is Route 32,
  which is *after* Falkner, not before. Worth a decision: accept Rock-only coverage into Falkner,
  or pull an Electric option earlier (e.g. onto Route 30/31) before finalizing these tables.
