# Violet City

See `documentation/areas/README.md` for what this doc format is and how to reproduce it for other
areas.

## Header facts

- **ENCDATA constant:** `ENCDATA_T22_VIOLET_CITY` (`data/Encounters.c:509`)
- **Map constant:** `MAP_T22` (`include/constants/maps.h:77`)
- **Connects:** Route 31 ↔ Route 32; also holds Sprout Tower (see below) and Falkner's gym.
- **Biome Map tie-in:** this is Falkner's home city (`HACK_PLAN.md`'s Biome Map row) — Flying-type,
  speed-control archetype. The town itself has no walking encounters (see below), so it doesn't
  contribute directly to the type-coverage pool; the approach routes/Dark Cave do that work.

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

**Surf (rate 15):** Poliwag (15–25), Poliwag (10–20), Poliwhirl (15–25), Poliwhirl (15–25), Poliwhirl (15–25).
**Old Rod (rate 25):** Magikarp (10), Magikarp (10), Magikarp (10), Poliwag (10), Poliwag (10).
**Good Rod (rate 50):** Magikarp (20), Poliwag (20), Poliwag (20), Poliwag (20), Poliwag (20).
**Super Rod (rate 75):** Poliwag (40), Poliwag (40), Magikarp (40), Poliwag (40), Magikarp (40).

## Rustling grass (Hoenn/Sinnoh sound species)

Not populated — no land tile here.

## Swarm

- `landSwarm = SPECIES_NONE`, `surfSwarm = SPECIES_POLIWAG`, `nightFish = SPECIES_POLIWAG`, `fishSwarm = SPECIES_POLIWHIRL`.
- **Active (fishing):** this map is in `sSwarmMapLUT` (`src/swarms.c:33`) — the Poliwhirl swarm fires here.

## Species summary

| Species | Type(s) | Regional Dex # | Method | Time |
|---|---|---|---|---|
| Magikarp | Water | 65 | Fish | — |
| Poliwag | Water | 346 | Surf, Fish, Swarm (surf), Fish (night) | — |
| Poliwhirl | Water | 347 | Surf, Swarm (fish) | — |

Dex numbers as of `data/RegionalDex.c` with 377 entries —
re-`grep` if the dex is renumbered.

## Notes

- **Resolved — early-game cleanup pass (after the Clair pass).** The active fishing swarm was
  Whiscash (dex-less); it's now **Poliwhirl**, matching Violet's existing Poliwag pond. Barboach/
  Whiscash stay out of the dex. Earlier notes below that describe these species as dex-less or intentionally kept are superseded.
- No land encounters at all — nothing to rework here for Pillar 2/3 purposes beyond the water
  table, which mirrors Route 30/31 and needs no separate decision unless those get changed.
- Whiscash dex-less is a `keep=No` sheet decision, not yet checked against this specific
  fish-swarm placement — low priority since it's swarm-only (rare, day-gated encounter), but worth
  a look whenever Water-type coverage for a *later* gym is being audited (Whiscash is Water/Ground,
  not relevant to Falkner).
