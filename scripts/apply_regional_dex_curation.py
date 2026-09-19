#!/usr/bin/env python3
"""Apply a dex-curation "keep" decision pass onto data/RegionalDex.c.

Takes a species_key / keep / first_region_encountered TSV (as pasted out of
the VG - Pokedex sheet's curation columns) and updates the regional dex:

  - keep == Yes  and species not yet in the dex -> added (appended in input
    order, i.e. roughly national dex order -- new entries land in a block at
    the end and should be hand-reordered/grouped later if desired).
  - keep == No   and species currently in the dex -> removed.
  - keep == Maybe, or blank/undecided               -> left untouched, and
    reported separately as still-open decisions.

The dex numbers are renumbered 1..N after add/remove so they stay contiguous
(required -- 0 means "not in regional dex").

Usage:
    python3 scripts/apply_regional_dex_curation.py CURATION_TSV [--apply]

Without --apply, only prints the report (dry run). With --apply, rewrites
data/RegionalDex.c.
"""

import argparse
import re
from collections import OrderedDict
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
REGIONAL_DEX_C = REPO_ROOT / "data" / "RegionalDex.c"
SPECIES_H = REPO_ROOT / "include" / "constants" / "species.h"

DEX_ENTRY_RE = re.compile(r"\[(SPECIES_\w+)\] = (\d+),")
SPECIES_DEFINE_RE = re.compile(r"^#define\s+(SPECIES_\w+)\b", re.MULTILINE)

HEADER = '''#include "../include/types.h"
#include "../include/config.h"
#include "../include/constants/species.h"

// defines the number for the species in the regional dex. 0 means not in regional dex
const u16 UNUSED RegionalDex[] =
{
'''
FOOTER = "};\n"


def parse_curation_tsv(path):
    decisions = OrderedDict()  # species_key -> "Yes" | "No" | "Maybe" | None
    regions = {}
    with path.open(encoding="utf-8") as f:
        lines = f.readlines()
    for line in lines[1:]:  # skip header
        line = line.rstrip("\n")
        if not line.strip():
            continue
        parts = line.split("\t")
        key = parts[0].strip()
        if not key.startswith("SPECIES_"):
            continue
        keep_raw = parts[1].strip() if len(parts) > 1 else ""
        region = parts[2].strip() if len(parts) > 2 else ""
        keep = {"yes": "Yes", "no": "No", "maybe": "Maybe"}.get(keep_raw.lower())
        decisions[key] = keep
        if region:
            regions[key] = region
    return decisions, regions


def parse_current_dex(path):
    text = path.read_text(encoding="utf-8")
    order = []
    for key, _num in DEX_ENTRY_RE.findall(text):
        order.append(key)
    return order


def known_species_keys(path):
    return set(SPECIES_DEFINE_RE.findall(path.read_text(encoding="utf-8")))


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("curation_tsv", type=Path)
    parser.add_argument("--apply", action="store_true", help="write data/RegionalDex.c (default: dry run)")
    args = parser.parse_args()

    decisions, regions = parse_curation_tsv(args.curation_tsv)
    current_order = parse_current_dex(REGIONAL_DEX_C)
    current_set = set(current_order)
    known = known_species_keys(SPECIES_H)

    unknown_keys = [k for k in decisions if k not in known]

    to_remove = [k for k in current_order if decisions.get(k) == "No"]
    to_add = [k for k, v in decisions.items() if v == "Yes" and k not in current_set]
    already_yes = [k for k, v in decisions.items() if v == "Yes" and k in current_set]
    noop_no = [k for k, v in decisions.items() if v == "No" and k not in current_set]
    maybe_list = [k for k, v in decisions.items() if v == "Maybe"]

    new_order = [k for k in current_order if k not in to_remove] + to_add

    print(f"Current dex size: {len(current_order)}")
    print(f"Adding {len(to_add)}: {', '.join(to_add) if to_add else '(none)'}")
    print(f"Removing {len(to_remove)}: {', '.join(to_remove) if to_remove else '(none)'}")
    print(f"Already Yes + already in dex (no-op): {len(already_yes)}")
    print(f"Already No + already absent (no-op): {len(noop_no)}")
    print(f"New dex size: {len(new_order)}")
    print(f"\n{len(maybe_list)} still-open 'Maybe' decisions (left untouched):")
    for k in maybe_list:
        print(f"  {k}")
    if unknown_keys:
        print(f"\nWARNING: {len(unknown_keys)} species_key(s) not found in species.h (typo?):")
        for k in unknown_keys:
            print(f"  {k}")

    if not args.apply:
        print("\nDry run only -- rerun with --apply to write data/RegionalDex.c")
        return

    lines = [HEADER]
    for i, key in enumerate(new_order, start=1):
        lines.append(f"    [{key}] = {i},\n")
    lines.append(FOOTER)
    REGIONAL_DEX_C.write_text("".join(lines), encoding="utf-8")
    print(f"\nWrote {REGIONAL_DEX_C.relative_to(REPO_ROOT)} ({len(new_order)} entries).")


if __name__ == "__main__":
    main()
