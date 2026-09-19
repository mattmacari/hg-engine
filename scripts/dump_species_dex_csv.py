#!/usr/bin/env python3
"""Dump data/Species.c + data/RegionalDex.c into a flat CSV for spreadsheet-based dex curation.

One row per species/form entry in data/Species.c, with its current regional dex
status (data/RegionalDex.c) attached. Intended to be imported into Google Sheets
to work through the Phase 1 dex curation pass by hand (mark species in/out,
re-sort dex numbers, etc.) rather than editing data/RegionalDex.c directly.

Usage:
    python3 scripts/dump_species_dex_csv.py [-o OUTPUT_CSV]

Defaults to data/generated/species_dex_dump.csv (gitignored, same as other
generated data in this repo).
"""

import argparse
import csv
import re
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
SPECIES_C = REPO_ROOT / "data" / "Species.c"
REGIONAL_DEX_C = REPO_ROOT / "data" / "RegionalDex.c"
DEFAULT_OUTPUT = REPO_ROOT / "data" / "generated" / "species_dex_dump.csv"

# Matches one top-level species/form entry in sSpeciesData, e.g.:
#     [SPECIES_CHIKORITA] = {
#         ...
#     },
# The closing "    }," is indented exactly 4 spaces, which only ever occurs at
# entry boundaries -- everything nested inside (.textData, .baseStats, etc.)
# is indented 8+ spaces, so this non-greedy match can't cross an entry boundary.
ENTRY_RE = re.compile(r"\[(SPECIES_\w+)\] = \{(.*?)\n {4}\},\n", re.DOTALL)

NAME_RE = re.compile(r'\.name = "([^"]*)"')
TYPES_RE = re.compile(r"\.types = \{ (TYPE_\w+), (TYPE_\w+) \}")
ABILITIES_RE = re.compile(r"\.abilities = \{ (ABILITY_\w+), (ABILITY_\w+) \}")
EGG_GROUPS_RE = re.compile(r"\.eggGroups = \{ (EGG_GROUP_\w+), (EGG_GROUP_\w+) \}")
CATCH_RATE_RE = re.compile(r"\.catchRate = (\d+)")
GENDER_RATIO_RE = re.compile(r"\.genderRatio = (-?\d+)")

BASE_STATS_RE = re.compile(
    r"\.baseStats = \{\s*"
    r"\.hp = (\d+),\s*"
    r"\.attack = (\d+),\s*"
    r"\.defense = (\d+),\s*"
    r"\.spAttack = (\d+),\s*"
    r"\.spDefense = (\d+),\s*"
    r"\.speed = (\d+),\s*\},"
)

REGIONAL_DEX_RE = re.compile(r"\[(SPECIES_\w+)\] = (\d+),")


def prettify(constant, prefix):
    """SPECIES_TYPHLOSION_HISUIAN, "SPECIES_" -> "Typhlosion Hisuian" """
    label = constant[len(prefix):] if constant.startswith(prefix) else constant
    return label.replace("_", " ").title()


def parse_species_c(text):
    entries = {}
    for match in ENTRY_RE.finditer(text):
        key, body = match.group(1), match.group(2)

        name_match = NAME_RE.search(body)
        # Form entries frequently leave .name as a "-----" placeholder and rely
        # on the base species name + form logic at runtime -- fall back to a
        # prettified constant name so the CSV still has something readable.
        raw_name = name_match.group(1) if name_match else ""
        name = raw_name if raw_name and raw_name != "-----" else prettify(key, "SPECIES_")

        types_match = TYPES_RE.search(body)
        type1 = ""
        type2 = ""
        if types_match:
            type1_raw, type2_raw = types_match.groups()
            type1 = prettify(type1_raw, "TYPE_")
            # Mono-type entries duplicate the same type in both slots.
            type2 = "" if type2_raw == type1_raw else prettify(type2_raw, "TYPE_")

        abilities_match = ABILITIES_RE.search(body)
        ability1 = ""
        ability2 = ""
        if abilities_match:
            a1, a2 = abilities_match.group(1), abilities_match.group(2)
            ability1 = "" if a1 == "ABILITY_NONE" else prettify(a1, "ABILITY_")
            ability2 = "" if a2 == "ABILITY_NONE" else prettify(a2, "ABILITY_")

        egg_match = EGG_GROUPS_RE.search(body)
        egg1 = ""
        egg2 = ""
        if egg_match:
            e1, e2 = egg_match.group(1), egg_match.group(2)
            egg1 = "" if e1 == "EGG_GROUP_NONE" else prettify(e1, "EGG_GROUP_")
            egg2 = "" if e2 == "EGG_GROUP_NONE" else prettify(e2, "EGG_GROUP_")

        catch_match = CATCH_RATE_RE.search(body)
        catch_rate = catch_match.group(1) if catch_match else ""

        gender_match = GENDER_RATIO_RE.search(body)
        gender_ratio = gender_match.group(1) if gender_match else ""

        stats_match = BASE_STATS_RE.search(body)
        if stats_match:
            hp, atk, dfn, spa, spd, spe = (int(x) for x in stats_match.groups())
            bst = hp + atk + dfn + spa + spd + spe
        else:
            hp = atk = dfn = spa = spd = spe = bst = ""

        entries[key] = {
            "species_key": key,
            "name": name,
            "type1": type1,
            "type2": type2,
            "ability1": ability1,
            "ability2": ability2,
            "hp": hp,
            "attack": atk,
            "defense": dfn,
            "sp_attack": spa,
            "sp_defense": spd,
            "speed": spe,
            "bst": bst,
            "catch_rate": catch_rate,
            "gender_ratio": gender_ratio,
            "egg_group1": egg1,
            "egg_group2": egg2,
        }
    return entries


def parse_regional_dex_c(text):
    return {key: int(num) for key, num in REGIONAL_DEX_RE.findall(text)}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "-o", "--output", type=Path, default=DEFAULT_OUTPUT,
        help=f"output CSV path (default: {DEFAULT_OUTPUT.relative_to(REPO_ROOT)})",
    )
    args = parser.parse_args()

    species = parse_species_c(SPECIES_C.read_text(encoding="utf-8"))
    regional_dex = parse_regional_dex_c(REGIONAL_DEX_C.read_text(encoding="utf-8"))

    fieldnames = [
        "species_key", "name", "type1", "type2", "ability1", "ability2",
        "hp", "attack", "defense", "sp_attack", "sp_defense", "speed", "bst",
        "catch_rate", "gender_ratio", "egg_group1", "egg_group2",
        "in_regional_dex", "regional_dex_number",
    ]

    args.output.parent.mkdir(parents=True, exist_ok=True)
    with args.output.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        for key, row in species.items():
            dex_number = regional_dex.get(key)
            row["in_regional_dex"] = dex_number is not None
            row["regional_dex_number"] = dex_number if dex_number is not None else ""
            writer.writerow(row)

    print(f"Wrote {len(species)} species/form entries to {args.output}")
    print(f"{len(regional_dex)} of those are currently in the regional dex.")


if __name__ == "__main__":
    main()
