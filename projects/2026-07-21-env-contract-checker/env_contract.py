#!/usr/bin/env python3
"""Validate a .env file against an example contract without exposing values."""

from __future__ import annotations

import argparse
import re
from dataclasses import dataclass
from pathlib import Path


KEY_PATTERN = re.compile(r"^[A-Za-z_][A-Za-z0-9_]*$")


@dataclass(frozen=True)
class Finding:
    severity: str
    code: str
    message: str


def parse_env(path: Path) -> tuple[set[str], list[Finding]]:
    keys: set[str] = set()
    findings: list[Finding] = []

    for line_number, raw_line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
        line = raw_line.strip()
        if not line or line.startswith("#"):
            continue
        if line.startswith("export "):
            line = line[7:].lstrip()
        if "=" not in line:
            findings.append(Finding("error", "malformed", f"line {line_number}: missing '='"))
            continue

        key, value = line.split("=", 1)
        key = key.strip()
        if not KEY_PATTERN.fullmatch(key):
            findings.append(Finding("error", "invalid-key", f"line {line_number}: invalid key name"))
            continue
        if key in keys:
            findings.append(Finding("error", "duplicate", f"line {line_number}: duplicate key {key}"))
        keys.add(key)

        value = value.strip()
        if value and not (value.startswith("'") or value.startswith('"')) and any(char.isspace() for char in value):
            findings.append(
                Finding("warning", "unquoted-space", f"line {line_number}: {key} contains unquoted whitespace")
            )

    return keys, findings


def check_contract(example_path: Path, actual_path: Path) -> list[Finding]:
    example_keys, findings = parse_env(example_path)
    actual_keys, actual_findings = parse_env(actual_path)
    findings.extend(actual_findings)

    for key in sorted(example_keys - actual_keys):
        findings.append(Finding("error", "missing", f"missing required key {key}"))
    for key in sorted(actual_keys - example_keys):
        findings.append(Finding("warning", "extra", f"unexpected key {key}"))
    return findings


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("example", type=Path, help="contract file, such as .env.example")
    parser.add_argument("actual", type=Path, help="environment file to validate")
    parser.add_argument("--strict", action="store_true", help="treat warnings as failures")
    args = parser.parse_args()

    try:
        findings = check_contract(args.example, args.actual)
    except (OSError, UnicodeError) as error:
        parser.error(str(error))

    for finding in findings:
        print(f"{finding.severity.upper()} [{finding.code}] {finding.message}")
    errors = sum(finding.severity == "error" for finding in findings)
    warnings = sum(finding.severity == "warning" for finding in findings)
    print(f"Checked contract: {errors} error(s), {warnings} warning(s)")
    return 1 if errors or (args.strict and warnings) else 0


if __name__ == "__main__":
    raise SystemExit(main())
