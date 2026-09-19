# Route 31

See `documentation/areas/README.md` for what this doc format is and how to reproduce it for other
areas.

## Header facts

- **ENCDATA constant:** `ENCDATA_R31_ROUTE_31` (`data/Encounters.c:409`)
- **Map constant:** `MAP_R31` (`include/constants/maps.h:39`)
- **Connects:** Route 30 ↔ Violet City; also the entrance to Dark Cave (see `Dark-Cave-Route-31-Entrance.md`)
- **Leads toward:** Falkner (Violet City) — final leg before the gym.
- **Biome Map tie-in:** explicitly called out in `HACK_PLAN.md`'s Falkner row — Rock counter comes
  from Geodude "via Dark Cave/Route 31, already vanilla-natural" (Geodude itself lives in the Dark
  Cave entrance off this route, not in Route 31's own table — see that doc). This route's own
  table doesn't carry Rock/Electric/Ice.

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
| 1 | 20 | 3 | Pidgey | Pidgey | Spinarak |
| 2 | 20 | 4 | Caterpie | Caterpie | Rattata |
| 3 | 10 | 3 | Pidgey | Pidgey | Spinarak |
| 4 | 10 | 4 | Caterpie | Caterpie | Rattata |
| 5 | 10 | 3 | Bellsprout | Bellsprout | Bellsprout |
| 6 | 10 | 3 | Bellsprout | Bellsprout | Bellsprout |
| 7 | 5 | 5 | Metapod | Metapod | Rattata |
| 8 | 5 | 5 | Metapod | Metapod | Rattata |
| 9 | 4 | 5 | Caterpie | Caterpie | Hoothoot |
| 10 | 4 | 5 | Metapod | Metapod | Hoothoot |
| 11 | 1 | 5 | Caterpie | Caterpie | Hoothoot |
| 12 | 1 | 5 | Metapod | Metapod | Hoothoot |

## Water/rod tables

**Surf (rate 15):** identical shape to Route 30 — Poliwag ×2 (60/30%), Poliwhirl ×3 (5/4/1%,
levels 15–25/15–25/32).
**Old Rod (60/30/5/4/1):** Magikarp ×3, Poliwag ×2 (all level 10)
**Good Rod (40/40/15/4/1):** Magikarp, Poliwag ×4 (all level 20)
**Super Rod (40/40/15/4/1):** Poliwag ×2, Magikarp ×2, Poliwag (all level 40)

## Rustling grass (Hoenn/Sinnoh sound species)

| Region | Slot 1 | Slot 2 |
|---|---|---|
| Hoenn | Whismur | Linoone |
| Sinnoh | Buizel | Bidoof |

## Swarm

- `landSwarm = SPECIES_PIDGEY`, `surfSwarm = SPECIES_POLIWAG`, `fishSwarm = SPECIES_MAGIKARP`,
  `nightFish = SPECIES_POLIWAG`
- **Inert:** `MAP_R31` is not in `sSwarmMapLUT` (`src/swarms.c`).

## Species summary

| Species | Type(s) | Regional Dex # | Method | Time |
|---|---|---|---|---|
| Pidgey | Normal/Flying | 10 | Walk | Morning/Day/Night |
| Caterpie | Bug | 20 | Walk | Morning/Day/Night |
| Metapod | Bug | 21 | Walk | Morning/Day/Night |
| Bellsprout | Grass/Poison | 57 | Walk | Morning/Day/Night |
| Spinarak | Bug/Poison | 28 | Walk | Night |
| Rattata | Normal | **not in regional dex** | Walk | Night |
| Hoothoot | Normal/Flying | 13 | Walk | Night |
| Poliwag | Water | 346 | Surf/Fish | — |
| Poliwhirl | Water | 347 | Surf | — |
| Magikarp | Water | 65 | Fish | — |
| Whismur | Normal | **not in regional dex** | Rustling grass (Hoenn) | — |
| Linoone | Normal | **not in regional dex** | Rustling grass (Hoenn) | — |
| Buizel | Water | **not in regional dex** | Rustling grass (Sinnoh) | — |
| Bidoof | Normal | **not in regional dex** | Rustling grass (Sinnoh) | — |

Dex numbers as of the full sheet-sync pass (`data/RegionalDex.c`, 366 entries) — re-`grep` if the
dex is renumbered again before this route's table is finalized.

## Notes

- **Rattata dex-less, same pattern as Routes 29/30** — 4 night slots (2, 4, 7, 8). Not resolved
  here; only Route 29's has been swapped so far. See [[feedback_dex_encounter_mismatches]].
- Bellsprout is the one land species unique to this route vs. Route 30 (all-day-parts, slots
  5–6) — matches the vanilla "forest edge approaching Violet City" read.
- **Type-coverage relevance (Pillar 3):** this route's own table still has no Rock/Electric/Ice —
  the Rock counter for Falkner comes from the adjacent Dark Cave entrance, not this table (see
  that doc). Worth re-running the full audit once all three Falkner-approach docs exist.
- Surf/fish tables are byte-for-byte identical to Route 30's — worth knowing if either gets
  rebalanced, since keeping them in sync (or deliberately diverging them) is a call worth making
  explicitly rather than by accident.
