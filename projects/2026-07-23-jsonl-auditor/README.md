# JSONL Auditor

A dependency-free command-line audit for JSON Lines files before they enter an
ingestion pipeline. It reports:

- malformed JSON with line and column numbers;
- blank lines and values that are not objects;
- duplicate values for a configurable identity field;
- the distinct object shapes found in the file.

## Run

```bash
python3 jsonl_auditor.py events.jsonl
python3 jsonl_auditor.py events.jsonl --id-field event_id
```

The report is emitted as JSON for easy CI integration. Exit code `0` means the
file has no issues, `1` means issues were found, and `2` means the file could
not be read.

## Verify

From the repository root:

```bash
python3 -m unittest discover projects/2026-07-23-jsonl-auditor -v
```
