# CSV Schema Drift Detector

A small command-line tool that compares two CSV files for added or removed columns and changes in inferred value types. It emits machine-readable JSON and returns exit code `1` when drift is found, making it useful in data-pipeline checks.

## Run the example

```bash
python3 schema_drift.py fixtures/baseline.csv fixtures/candidate.csv
```

## Verify

From the repository root:

```bash
python3 -m unittest discover projects/2026-07-20-csv-schema-drift-detector -v
```

The tool uses only the Python standard library.
