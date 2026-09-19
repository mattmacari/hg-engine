# Wild Encounter Data Structure

Reference doc for `data/Encounters.c` — the file that drives Pillar 2/3 work (biome-matched wild
encounters, type-coverage audit). Written for quick orientation by future devs/agents working
through the Milestone 4+ gym/route rework; supplements (doesn't replace)
`documentation/wiki/Wild-Pokémon-Table-Documentation.md`, which is still accurate on structure but
doesn't cover the swarm/sound mechanics or this repo's per-field details below.

## Files involved

| File | Role |
|---|---|
| `include/encounter.h` | C struct definitions (`EncounterData`, `LandEncounterData`, `EncounterDataSlot`). |
| `include/constants/encounter_tables.h` | `enum EncounterAreaId` — one `ENCDATA_<mapcode>_<NAME>` constant per area, in array-index order. |
| `data/Encounters.c` | The actual data: `const EncounterData __data[]`, designated-initializer indexed by `ENCDATA_*`. |
| `data/SafariEncounters.c` + `include/safari_encounter.h` | **Separate, differently-shaped struct** for the Goldenrod Safari Zone only (per-area land/surf/rod tables with "bonus" unlockable slots). Not covered by this doc — the Safari Zone isn't part of the Pillar 2/3 route work. |
| `data/Headbutt.c` | Headbutt-tree encounters. Also separate from `EncounterData` — not part of this struct. |

## Struct layout

```c
typedef struct PACKED EncounterData {
    u8 rateWalk;
    u8 rateSurf;
    u8 rateRockSmash;
    u8 rateOldRod;
    u8 rateGoodRod;
    u8 rateSuperRod;
    u8 dummy[2];
    LandEncounterData landSlots;
    u16 hoennSoundSpecies[2];
    u16 sinnohSoundSpecies[2];
    EncounterDataSlot surfSlots[5];
    EncounterDataSlot rockSmashSlots[2];
    EncounterDataSlot oldRodSlots[5];
    EncounterDataSlot goodRodSlots[5];
    EncounterDataSlot superRodSlots[5];
    u16 landSwarm;
    u16 surfSwarm;
    u16 nightFish;
    u16 fishSwarm;
} EncounterData;

typedef struct PACKED LandEncounterData {
    u8 levels[12];
    u16 speciesMorning[12];
    u16 speciesDay[12];
    u16 speciesNight[12];
} LandEncounterData;

typedef struct PACKED EncounterDataSlot {
    u8 levelMin;
    u8 levelMax;
    u16 species;
} EncounterDataSlot;
```

One `EncounterData` entry = one map/area. Every species field is form-aware (stored as
`form << 11 | species`) — use the `monwithform`-equivalent helper in whatever tooling writes these
if a non-default form needs to appear wild.

## Field reference

### Encounter-method rates

`rateWalk` / `rateSurf` / `rateRockSmash` / `rateOldRod` / `rateGoodRod` / `rateSuperRod` — per-step
(or per-cast, for fishing) chance of triggering an encounter via that method in this area. `0`
disables that method entirely for the area (e.g. an indoor/town entry with no grass sets
`rateWalk = 0`). Higher = more frequent. These are relative weights from vanilla Gen 4/HGSS, not
independently tunable percentages with a documented formula in this repo — treat existing vanilla
values (25 walk / 15 surf / 25-50-75 old-good-super rod is a common baseline) as the reference point
when an area's rates aren't being deliberately changed.

### Land encounters (`landSlots`)

- `levels[12]` — **one fixed level per slot** (not a min/max range, unlike surf/fish slots below).
  Shared across morning/day/night for a given slot index.
- `speciesMorning` / `speciesDay` / `speciesNight` — 12 species each, indexed by the same slot
  positions as `levels`. Time-of-day windows are the standard HGSS ones (morning/day/night).
- **Slot probabilities are fixed by slot index** (not stored in the struct — this is an engine
  constant from the original game, same order every table):

  | Slot | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 |
  |---|---|---|---|---|---|---|---|---|---|---|---|---|
  | % | 20 | 20 | 10 | 10 | 10 | 10 | 5 | 5 | 4 | 4 | 1 | 1 |

  Put the area's "common" species in slots 1–2, secondary common in 3–6, uncommon in 7–8, rare in
  9–10, rarest in 11–12. This is the main lever for "what does this route feel like ecologically."

### Surf / Rock Smash / Fishing (`EncounterDataSlot[]` arrays)

Each slot has an independent `levelMin`/`levelMax` range (unlike land slots). Fixed slot
probabilities:

| Method | Slots | % per slot |
|---|---|---|
| Surf | 5 | 60, 30, 5, 4, 1 |
| Rock Smash | 2 | 90, 10 |
| Old Rod | 5 | 60, 30, 5, 4, 1 |
| Good Rod | 5 | 40, 40, 15, 4, 1 |
| Super Rod | 5 | 40, 40, 15, 4, 1 |

Set all slots to `{ 0, 0, SPECIES_NONE }` for a method that isn't available in that area (matches
`rate* = 0` above).

### Rustling-grass "sound" encounters (`hoennSoundSpecies` / `sinnohSoundSpecies`)

HGSS-specific mechanic: patches of grass can "rustle," and searching them gives a Hoenn- or
Sinnoh-dex species not otherwise available in Johto/Kanto (a legacy-game nod). 2 slots each,
independent of the land table's time-of-day/level system — species only, no level field (level is
presumably fixed/derived elsewhere in the original engine, not exposed in this struct). Good spot
to place an ecologically-fitting "surprise" species per area without touching the main land table.

### Swarms (`landSwarm` / `surfSwarm` / `fishSwarm`)

Feeds the vanilla **daily route swarm** mechanic (`src/swarms.c`): each day, one of a **fixed list
of 20 maps** (`sSwarmMapLUT` in `src/swarms.c`) gets a swarm of the species stored in this field,
announced in-game. **Only meaningful for maps already in that 20-map list** — setting
`landSwarm`/etc. on an area outside that list has no effect (nothing reads it). Don't rely on these
fields for arbitrary areas; check `sSwarmMapLUT` first if a swarm placement matters for a
biome/counter-access decision.

### `nightFish`

Present in the struct but **not referenced by any C code in this repo** (`grep`-confirmed against
`src/`, `armips/`, `include/`) — appears to be an inert vanilla leftover field. Don't rely on it
doing anything; if a "special night fishing" mechanic is ever wanted, it would need new engine work,
not just populating this field.

### `dummy[2]`

Padding for struct alignment. Not species/data — ignore.

## Area indexing (`ENCDATA_*`)

`include/constants/encounter_tables.h` defines one `ENCDATA_<mapcode>_<NAME>` per area; the numeric
value is that area's index into `data/Encounters.c`'s `__data[]` array (designated initializers, so
`data/Encounters.c` doesn't need to list them in order, but the enum itself is declared in index
order for readability). Naming convention: `T##` = town, `R##` = route, `D##R####` = dungeon/cave
sub-area (matches the game's internal map-file naming, not a convention invented by this repo).

**Important:** this index is *not* the same as the map's `MAP_*` ID in
`include/constants/maps.h` (e.g. `MAP_R30 == 34` but `ENCDATA_R30_ROUTE_30 == 3`). Which `ENCDATA_*`
index a given physical map actually uses is a field on that map's header data, which lives outside
this repo's tracked source (edited via an external map tool like DSPRE — see CLAUDE.md's
"Not in this repo: map/overworld editing"). For all currently-existing maps this mapping already
matches vanilla, so in practice: **find the map's existing `ENCDATA_*` entry by name/grep, don't try
to compute or reassign the index.**

## Falkner-area entries (for reference)

| Constant | data/Encounters.c line (as of dex-curation commit) |
|---|---|
| `ENCDATA_R30_ROUTE_30` | 309 |
| `ENCDATA_R31_ROUTE_31` | 409 |
| `ENCDATA_T22_VIOLET_CITY` | 509 |
| `ENCDATA_R32_ROUTE_32` | 809 |
| `ENCDATA_D42R0102_DARK_CAVE_ROUTE_31_ENTRANCE` | 6909 |

Line numbers will drift as the file is edited — re-`grep` `ENCDATA_` rather than trusting these
long-term.
