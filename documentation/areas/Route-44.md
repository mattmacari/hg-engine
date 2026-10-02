# Route 44

See `documentation/areas/README.md` for what this doc format is and how to reproduce it for other
areas.

## Header facts

- **ENCDATA constant:** `ENCDATA_R44_ROUTE_44` (`data/Encounters.c:5909`)
- **Map constant:** `MAP_R44` (`include/constants/maps.h:50`)
- **Connects:** Mahogany Town (west) ↔ Ice Path (east).
- **Leads toward:** Clair (Blackthorn City) — first leg of the approach, through Ice Path.
- **Biome Map tie-in:** none directly; a wooded lakeside route with a grass core (Tangela/Bellsprout
  line) and Lickitung.

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
| 1 | 20 | 23 | Tangela | Tangela | Tangela |
| 2 | 20 | 22 | Weepinbell | Weepinbell | Weepinbell |
| 3 | 10 | 23 | Tangela | Tangela | Tangela |
| 4 | 10 | 22 | Weepinbell | Weepinbell | Weepinbell |
| 5 | 10 | 22 | Bellsprout | Bellsprout | Bellsprout |
| 6 | 10 | 22 | Bellsprout | Bellsprout | Bellsprout |
| 7 | 5 | 24 | Lickitung | Lickitung | Lickitung |
| 8 | 5 | 24 | Lickitung | Lickitung | Lickitung |
| 9 | 4 | 24 | Weepinbell | Weepinbell | Weepinbell |
| 10 | 4 | 26 | Lickitung | Lickitung | Lickitung |
| 11 | 1 | 24 | Weepinbell | Weepinbell | Weepinbell |
| 12 | 1 | 26 | Lickitung | Lickitung | Lickitung |

## Water/rod tables

**Surf (rate 10):** Poliwag (20–30), Poliwag (15–25), Poliwhirl (20–30), Poliwhirl (20–30), Poliwhirl (20–30).
**Old Rod (rate 25):** Magikarp (10), Magikarp (10), Magikarp (10), Poliwag (10), Poliwag (10).
**Good Rod (rate 50):** Magikarp (20), Poliwag (20), Horsea (20), Poliwag (20), Remoraid (20).
**Super Rod (rate 75):** Poliwag (40), Horsea (40), Magikarp (40), Remoraid (40), Seadra (40).

## Rustling grass (Hoenn/Sinnoh sound species)

| Region | Slot 1 | Slot 2 |
|---|---|---|
| Hoenn | Whismur | Linoone |
| Sinnoh | Buizel | Bidoof |

## Swarm

- `landSwarm = SPECIES_TANGELA`, `surfSwarm = SPECIES_POLIWAG`, `nightFish = SPECIES_POLIWAG`, `fishSwarm = SPECIES_REMORAID`.
- **Active (fishing only):** `MAP_R44` is in `sSwarmMapLUT` (`src/swarms.c:26`, `SWARM_FISHING`) — the Remoraid fish swarm fires; the land/surf swarm fields are inert.

## Species summary

| Species | Type(s) | Regional Dex # | Method | Time |
|---|---|---|---|---|
| Bellsprout | Grass/Poison | 57 | Walk | Morning/Day/Night |
| Weepinbell | Grass/Poison | 58 | Walk | Morning/Day/Night |
| Magikarp | Water | 65 | Fish | — |
| Remoraid | Water | 130 | Fish, Swarm (fish) | — |
| Lickitung | Normal | 136 | Walk | Morning/Day/Night |
| Tangela | Grass | 138 | Walk, Swarm (land) | Morning/Day/Night |
| Poliwag | Water | 346 | Surf, Fish, Swarm (surf), Fish (night) | — |
| Poliwhirl | Water | 347 | Surf | — |
| Horsea | Water | 370 | Fish | — |
| Seadra | Water | 371 | Fish | — |
| Bidoof | Normal | **not in dex** | Rustling grass (Sinnoh) | — |
| Buizel | Water | **not in dex** | Rustling grass (Sinnoh) | — |
| Linoone | Normal | **not in dex** | Rustling grass (Hoenn) | — |
| Whismur | Normal | **not in dex** | Rustling grass (Hoenn) | — |

Dex numbers as of `data/RegionalDex.c` with 374 entries (Horsea/Seadra/Kingdra/Swablu/Altaria added as #370–374 in the Clair pass) —
re-`grep` if the dex is renumbered.

## Notes

- The land table was already clean (every species dex-tracked); no land changes.
- **New — Horsea/Seadra added to the rods.** Kingdra is Clair's signature, but the Horsea line
  wasn't in the regional dex or catchable before her gym. It was added to the dex (#370–372) and
  placed here:
  - Good Rod slot 3 (Poliwag → **Horsea**).
  - Super Rod slot 2 (Poliwag → **Horsea**).
  - Super Rod slot 5 (Magikarp → **Seadra**, the 1% rare slot).
  This sits next to Remoraid, the route's existing sea-creature rod species and active fish swarm.
- **Left as-is:** dex-less rustling-grass species (post-game only).
