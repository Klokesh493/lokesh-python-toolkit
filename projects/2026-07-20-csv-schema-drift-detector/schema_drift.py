#!/usr/bin/env python3
"""Compare the columns and inferred value types of two CSV files."""

from __future__ import annotations

import argparse
import csv
import json
from collections import Counter
from pathlib import Path


def value_type(value: str) -> str:
    value = value.strip()
    if not value:
        return "empty"
    if value.lower() in {"true", "false"}:
        return "boolean"
    try:
        int(value)
        return "integer"
    except ValueError:
        pass
    try:
        float(value)
        return "number"
    except ValueError:
        return "text"


def profile(path: Path) -> dict[str, Counter[str]]:
    with path.open(newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle)
        if reader.fieldnames is None:
            raise ValueError(f"{path} has no header row")
        columns = {name: Counter() for name in reader.fieldnames}
        for row in reader:
            for name in reader.fieldnames:
                columns[name][value_type(row.get(name, ""))] += 1
    return columns


def compare(baseline: Path, candidate: Path) -> dict[str, object]:
    before = profile(baseline)
    after = profile(candidate)
    before_names, after_names = set(before), set(after)
    shared = before_names & after_names
    changed = {}
    for name in sorted(shared):
        old_types = set(before[name]) - {"empty"}
        new_types = set(after[name]) - {"empty"}
        if old_types != new_types:
            changed[name] = {
                "baseline": sorted(old_types),
                "candidate": sorted(new_types),
            }
    return {
        "added_columns": sorted(after_names - before_names),
        "removed_columns": sorted(before_names - after_names),
        "changed_types": changed,
        "drift_detected": bool(
            (after_names - before_names) or (before_names - after_names) or changed
        ),
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("baseline", type=Path)
    parser.add_argument("candidate", type=Path)
    args = parser.parse_args()
    result = compare(args.baseline, args.candidate)
    print(json.dumps(result, indent=2))
    return 1 if result["drift_detected"] else 0


if __name__ == "__main__":
    raise SystemExit(main())
