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
| Walk | 0 | No — town, no grass |
| Surf | 15 | Yes |
| Rock Smash | 0 | No |
| Old Rod | 25 | Yes |
| Good Rod | 50 | Yes |
| Super Rod | 75 | Yes |

## Water/rod tables

**Surf (rate 15):** Poliwag ×2 (60/30%, levels 15–25/10–20), Poliwhirl ×3 (5/4/1%, all levels
15–25). Slightly different from Route 30/31's surf table, where the rarest (1%) slot narrows to a
fixed level 32 — here all three Poliwhirl slots keep the wider 15–25 range.
**Old Rod (60/30/5/4/1):** Magikarp ×3, Poliwag ×2 (all level 10)
**Good Rod (40/40/15/4/1):** Magikarp, Poliwag ×4 (all level 20)
**Super Rod (40/40/15/4/1):** Poliwag ×2, Magikarp ×2, Poliwag (all level 40)

Fishing tables are otherwise the same Poliwag/Poliwhirl/Magikarp shape as Routes 30/31 — this is
the same river system running through town.

## Swarm

- `landSwarm = SPECIES_NONE`, `surfSwarm = SPECIES_POLIWAG`, `nightFish = SPECIES_POLIWAG`,
  `fishSwarm = SPECIES_WHISCASH`
- **Active:** `MAP_T22` **is** in `sSwarmMapLUT` (`src/swarms.c`, `SWARM_FISHING` type) — on the
  days this map rolls, the swarm gives Whiscash via `fishSwarm`, not the usual fishing-rod table.
  Second area found so far (after the Dark Cave Route 31 entrance) where this field is live.

## Species summary

| Species | Type(s) | Regional Dex # | Method | Time |
|---|---|---|---|---|
| Poliwag | Water | 346 | Surf/Fish | — |
| Poliwhirl | Water | 347 | Surf | — |
| Magikarp | Water | 65 | Fish | — |
| Whiscash | Water/Ground | **not in regional dex** | Fish swarm only | — |

Dex numbers as of the full sheet-sync pass (`data/RegionalDex.c`, 366 entries) — re-`grep` if the
dex is renumbered again before this area's table is finalized.

## Notes

- No land encounters at all — nothing to rework here for Pillar 2/3 purposes beyond the water
  table, which mirrors Route 30/31 and needs no separate decision unless those get changed.
- Whiscash dex-less is a `keep=No` sheet decision, not yet checked against this specific
  fish-swarm placement — low priority since it's swarm-only (rare, day-gated encounter), but worth
  a look whenever Water-type coverage for a *later* gym is being audited (Whiscash is Water/Ground,
  not relevant to Falkner).
