# Route 40

See `documentation/areas/README.md` for what this doc format is and how to reproduce it for other
areas.

## Header facts

- **ENCDATA constant:** `ENCDATA_W40_ROUTE_40` (`data/Encounters.c:4109`)
- **Map constant:** `MAP_W40` (`include/constants/maps.h:98`)
- **Connects:** Olivine City (north) ↔ Cianwood City (south), with a Whirl Islands side-entrance
  (`MAP_W40R0101`) reachable off this route.
- **Leads toward:** Chuck (Cianwood City) — first leg of the Olivine→Cianwood sea crossing (Route
  40 → Route 41 → Cianwood City). Pure water route — no land tile at all (`rateWalk = 0`).
- **Biome Map tie-in:** `HACK_PLAN.md`'s Chuck row calls Cianwood "a stormy coastal island reached
  by Surf — genuinely fits a rain/ocean archetype." This route is that crossing.

## Encounter methods active

| Method | Rate | Active? |
|---|---|---|
| Walk | 0 | No (pure water route, no land tile) |
| Surf | 10 | Yes |
| Rock Smash | 0 | No |
| Old Rod | 25 | Yes |
| Good Rod | 50 | Yes |
| Super Rod | 75 | Yes |

## Water/rod tables

**Surf (rate 10):** Staryu ×2 (15/10%), Starmie ×3 (15/15/15%).
**Old Rod (10/10/10/10/10):** Magikarp ×3, Shellder ×2 (all level 10).
**Good Rod (20/20/20/20/20):** Magikarp, Shellder ×3, Corsola (all level 20).
**Super Rod (40/40/40/40/40):** Shellder ×3, Corsola, Cloyster (all level 40).

## Rustling grass (Hoenn/Sinnoh sound species)

Not populated — no land tile on this route.

## Swarm

- `surfSwarm = SPECIES_STARYU`, `nightFish = SPECIES_STARYU`, `fishSwarm = SPECIES_MAGIKARP`.
  `landSwarm = SPECIES_NONE` (no grass tile to swarm on).
- **Inert:** `MAP_W40` is not in `sSwarmMapLUT` (`src/swarms.c`).

## Species summary

| Species | Type(s) | Regional Dex # | Method | Time |
|---|---|---|---|---|
| Magikarp | Water | 65 | Fish, Swarm (fish) | — |
| Corsola | Water/Rock | 129 | Fish | — |
| Staryu | Water | 125 | Surf, Fish (night), Swarm (surf) | — |
| Starmie | Water/Psychic | 126 | Surf | — |
| Shellder | Water/Ice | 127 | Fish | — |
| Cloyster | Water/Ice | 128 | Fish | — |

Dex numbers as of the full sheet-sync pass (`data/RegionalDex.c`, 368 entries) — re-`grep` if the
dex is renumbered again before this route's table is finalized.

## Notes

- **Resolved — Tentacool/Tentacruel replaced (100% of the Surf table).** They were dex-less and,
  since this is a pure water route, effectively *were* the route. Replaced with **Staryu/Starmie**
  instead of introducing new flavor — Staryu was already this route's `nightFish`, so this just
  promotes a species already meant to be here into its full Surf role; Starmie (#126) fills the
  rarer/evolved slots.
- **Resolved — Krabby/Kingler replaced across the rod tables (40–80% of each tier).** Replaced with
  **Shellder/Cloyster** — Shellder was already established one route over on Route 41, so this
  unifies the whole Olivine↔Cianwood crossing into one coherent marine ecosystem instead of three
  separate incoherent fillers (see Route-41.md and Cianwood-City.md for the matching fix).
- This route has no land tile, so it contributes nothing to Chuck's Flying/Psychic/Fairy
  counter-access question — see Cianwood-City.md's Notes for the full coverage-audit writeup
  (already resolved, no gap).
- Whirl Islands (`MAP_W40R0101` and floors below) is reachable off this route but is optional,
  postgame-adjacent legendary content (Lugia) — not covered by this doc; flag separately if it
  needs its own pass.
