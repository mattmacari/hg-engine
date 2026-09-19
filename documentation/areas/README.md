# Area/Route Docs

One file per route/area we touch during the Phase 1 gym/biome rework (see `HACK_PLAN.md`
Milestone 4). Each doc is a snapshot of that area's **current** (pre-rework, usually
still-vanilla) wild encounter data plus enough cross-referenced context (regional dex status,
swarm/rustling-grass gotchas, type-coverage relevance) to make edits to `data/Encounters.c`
fast and low-risk. Re-generate/update the doc after the area's table is actually changed — these
are working notes, not a permanent record of vanilla data.

Use `Route-29.md` as the template. Sections, in order:

1. **Header facts** — `ENCDATA_*` constant + `data/Encounters.c` line, connecting areas, which
   gym/milestone this area feeds into, biome-map tie-in if any (per `HACK_PLAN.md`'s Biome Map
   table).
2. **Encounter methods active** — which of walk/surf/rock smash/old-good-super rod have a nonzero
   rate here, straight from the struct (see
   `documentation/Encounter-Data-Structure.md` for field meanings).
3. **Land encounter table** — full 12-slot morning/day/night breakdown with the fixed slot
   probabilities and per-slot level.
4. **Water/rod tables** — surf/rock smash/fishing slots, if active.
5. **Rustling grass (Hoenn/Sinnoh sound species)** — if populated.
6. **Swarm** — `landSwarm`/`surfSwarm`/`fishSwarm` values, and whether this area is actually in
   `sSwarmMapLUT` (`src/swarms.c`) for the field to do anything.
7. **Species summary table** — every species appearing anywhere above, with type(s) and current
   regional dex number (or flagged as not-in-dex) pulled from `data/RegionalDex.c`.
8. **Notes** — bullet list of anything relevant but not tabular: dex/encounter mismatches, type-
   coverage audit relevance (Pillar 3), swarm-field gotchas, anything that needs a decision before
   this area's table gets rewritten.
