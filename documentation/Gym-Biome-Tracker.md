# Gym/Biome Rework Tracker (Phase 1 — Johto)

Working checklist for Milestones 2–4 in `HACK_PLAN.md` (biome map → dex curation → gym rebuild),
tracked per gym/boss instead of as one big pass. Update this table as each gym's work lands —
check off steps and link the area doc(s) once they exist under `documentation/areas/`.

Per-gym steps (see `HACK_PLAN.md` Technical Approach + Milestones for what each means):
1. **Area docs** — encounter-data snapshots for the routes/areas feeding into this gym
   (`documentation/areas/`, format per `documentation/areas/README.md`).
2. **Encounters reworked** — `data/Encounters.c` (+ `data/SafariEncounters.c` if relevant) edited
   to match the biome.
3. **Dex synced** — `data/RegionalDex.c` updated to match the curation sheet for species touched
   by this gym's areas.
4. **Type-coverage audit** — Pillar 3 check run/confirmed for this gym (counter-type access before
   reaching it).
5. **Trainer rebuild** — `data/Trainers.c` roster rebuilt around the gym's archetype.

## Johto gyms

| # | Gym / Boss | Type / Archetype | Area docs | Encounters | Dex synced | Coverage audit | Trainer rebuild |
|---|---|---|---|---|---|---|---|
| 1 | **Falkner** (Violet City) | Flying — Tailwind speed control | [Sprout Tower](areas/Sprout-Tower.md), [Violet City](areas/Violet-City.md), [Route 29](areas/Route-29.md), [Route 30](areas/Route-30.md), [Route 31](areas/Route-31.md), [Dark Cave (Route 31 entrance)](areas/Dark-Cave-Route-31-Entrance.md) | ✅ | ✅ | ✅ (per commit log) | ✅ |
| 2 | **Bugsy** (Azalea Town) | Bug — hazard-setting swarm | [Route 32](areas/Route-32.md), [Ruins of Alph](areas/Ruins-of-Alph.md), [Union Cave](areas/Union-Cave.md), [Route 33](areas/Route-33.md), [Slowpoke Well](areas/Slowpoke-Well.md), [Ilex Forest](areas/Ilex-Forest.md) | ✅ | ✅ | ✅ | ✅ |
| 3 | **Whitney** (Goldenrod City) | Normal — bulky pivot / status-stall | — | ⬜ | ⬜ | ⬜ | ⬜ |
| 4 | **Morty** (Ecruteak City) | Ghost — Trick Room / burn stall | — | ⬜ | ⬜ | ⬜ | ⬜ |
| 5 | **Chuck** (Cianwood City) | Fighting — rain abuse | — | ⬜ | ⬜ | ⬜ | ⬜ |
| 6 | **Jasmine** (Olivine City) | Steel — defensive wall core + signature double (Steel/Electric) | — | ⬜ | ⬜ | ⬜ | ⬜ |
| 7 | **Pryce** (Mahogany Town) | Ice — hail support / bulky wall | — | ⬜ | ⬜ | ⬜ | ⬜ |
| 8 | **Clair** (Blackthorn City) | Dragon — Dragon Dance power core + signature double (Dragon/Fairy-Steel) | — | ⬜ | ⬜ | ⬜ | ⬜ |

## Elite Four, Champion, Rival

Indoor/character-driven fights (Indigo Plateau) — no biome/encounter work, so only the trainer
rebuild + coverage-audit steps apply. Tracked separately since they don't fit the area-doc flow
above.

| Trainer | Type / Archetype | Coverage audit | Trainer rebuild |
|---|---|---|---|
| **Will** | Psychic — bulky special core, Calm Mind | ⬜ | ⬜ |
| **Koga** | Poison — trapping/hazard stall | ⬜ | ⬜ |
| **Bruno** | Fighting — physical power core, priority + setup | ⬜ | ⬜ |
| **Karen** | Dark — mixed-attacker pressure core | ⬜ | ⬜ |
| **Lance** (Champion) | Dragon — apex power core, showcase Mega | ⬜ | ⬜ |
| **Silver** (Rival) | Mixed, adapts to counter the player | ⬜ | ⬜ (recurring — multiple encounters, see `HACK_PLAN.md`) |

## Notes

- Full rationale (biome fit, archetype reasoning, counter-access notes) for every row lives in
  `HACK_PLAN.md`'s Biome Map table — this doc is just the *progress* view, don't duplicate the
  reasoning here.
- Route/area names for gyms 2–8 aren't filled in yet — add them as each gym's encounter-audit pass
  starts, rather than guessing ahead of time.
- Milestone 5 (starter swap) and Milestone 6 (trainer competency pass) aren't per-gym in the same
  way; they stay tracked directly in `HACK_PLAN.md`.
