# Lokesh Python Toolkit runbook

## What the project does

Small operational checks are hard to reuse when their inputs and tests are scattered. Each utility needs a documented command and an isolated fixture.

See the [architecture and data flow](ARCHITECTURE.md) and [project case study](CASE_STUDY.md).

## Run from a clean checkout

Use Python 3 and Make. Install the pinned developer tools in a local environment.

```sh
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements-dev.txt
```

Choose a utility from the [project index](../README.md) and run its sample command.

## Expected result

Each utility test suite reports its own pass or failure.

## Verify a change

Run `make check PYTHON=python` inside the virtual environment. This runs the application checks, Ruff lint, and the Bandit static gate.
The [development guide](DEVELOPMENT.md) explains the tools and the [local report](../reports/devsecops.md) records what passed.

## If a check fails

Run the first failing command on its own. For a replay mismatch, inspect the diff and compare the input, rule, and expected output before updating the baseline.
For a lint or Bandit finding, review the reported source line and rerun the relevant target.

## Golden note

Start with the specific utility fixture and its test command when a collection-wide check fails.

## Operating limits

Use the [case study](CASE_STUDY.md) to check assumptions before applying a result to a live environment.
