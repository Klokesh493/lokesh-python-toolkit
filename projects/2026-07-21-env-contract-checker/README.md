# Env Contract Checker

Validate a `.env` file against `.env.example` without printing secret values. The checker reports missing and unexpected keys, duplicate assignments, invalid key names, malformed lines, and unquoted whitespace.

## Run

```bash
python3 env_contract.py .env.example .env
```

Add `--strict` to make warnings fail the check. Exit status is nonzero for errors (or warnings in strict mode), making the command suitable for CI and preflight scripts.

## Verify

From the repository root:

```bash
python3 -m unittest discover projects/2026-07-21-env-contract-checker -v
```
