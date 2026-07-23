#!/usr/bin/env python3
"""Audit JSON Lines files for common ingestion problems."""

from __future__ import annotations

import argparse
import json
import sys
from collections import Counter
from pathlib import Path
from typing import TextIO


def audit(stream: TextIO, id_field: str = "id") -> dict[str, object]:
    """Return a JSON-serializable audit report for a JSON Lines stream."""
    records = 0
    blank_lines: list[int] = []
    malformed: list[dict[str, object]] = []
    non_objects: list[int] = []
    shapes: Counter[tuple[str, ...]] = Counter()
    seen_ids: dict[str, int] = {}
    duplicate_ids: list[dict[str, object]] = []

    for line_number, raw_line in enumerate(stream, start=1):
        if not raw_line.strip():
            blank_lines.append(line_number)
            continue

        try:
            value = json.loads(raw_line)
        except json.JSONDecodeError as error:
            malformed.append(
                {
                    "line": line_number,
                    "column": error.colno,
                    "message": error.msg,
                }
            )
            continue

        records += 1
        if not isinstance(value, dict):
            non_objects.append(line_number)
            continue

        shapes[tuple(sorted(value))] += 1
        if id_field in value:
            identity = json.dumps(
                value[id_field], sort_keys=True, separators=(",", ":")
            )
            if identity in seen_ids:
                duplicate_ids.append(
                    {
                        "value": value[id_field],
                        "first_line": seen_ids[identity],
                        "line": line_number,
                    }
                )
            else:
                seen_ids[identity] = line_number

    shape_report = [
        {"fields": list(fields), "count": count}
        for fields, count in sorted(
            shapes.items(), key=lambda item: (-item[1], item[0])
        )
    ]
    issue_count = (
        len(blank_lines) + len(malformed) + len(non_objects) + len(duplicate_ids)
    )

    return {
        "records": records,
        "issues": issue_count,
        "blank_lines": blank_lines,
        "malformed": malformed,
        "non_object_lines": non_objects,
        "duplicate_ids": duplicate_ids,
        "shapes": shape_report,
    }


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Audit a JSON Lines file for ingestion problems."
    )
    parser.add_argument("path", type=Path, help="JSONL file to audit")
    parser.add_argument(
        "--id-field",
        default="id",
        help="field used to detect duplicate records (default: id)",
    )
    return parser


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    try:
        with args.path.open(encoding="utf-8") as stream:
            report = audit(stream, args.id_field)
    except OSError as error:
        print(f"jsonl-auditor: {error}", file=sys.stderr)
        return 2

    print(json.dumps(report, indent=2, ensure_ascii=False))
    return 1 if report["issues"] else 0


if __name__ == "__main__":
    raise SystemExit(main())
