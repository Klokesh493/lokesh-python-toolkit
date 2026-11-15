# Skills and verification

## What this repository demonstrates

Test isolation across independent CLI utilities and reproducible checks using the Python standard library.

## Reproduce the result

Run `make verify` to exercise the dated utility suites individually.

Run `make verify` locally. Ruff and Bandit medium/high checks passed for the checked Python code.

## Scope

Each utility has its own input contract and exit behavior.

[projects/2026-06-24-markdown-link-checker/markdown_link_checker.py](../projects/2026-06-24-markdown-link-checker/markdown_link_checker.py) · [projects/2026-06-24-markdown-link-checker/test_markdown_link_checker.py](../projects/2026-06-24-markdown-link-checker/test_markdown_link_checker.py) · [projects/2026-06-24-task-triage-cli/task_triage.py](../projects/2026-06-24-task-triage-cli/task_triage.py) · [projects/2026-06-24-task-triage-cli/test_task_triage.py](../projects/2026-06-24-task-triage-cli/test_task_triage.py) · [Architecture](../docs/ARCHITECTURE.md) · [Case study](../docs/CASE_STUDY.md) · [Runbook](../docs/RUNBOOK.md) · [CI template](../docs/github-actions/ci.yml)
