# Lokesh Python Toolkit

A collection of small, runnable Python projects built to practice useful engineering habits: clear inputs, readable outputs, tests, sample files, and simple verification commands.

## Recent Builds

| Date | Project | What it does | Verification |
| --- | --- | --- | --- |
| 2026-07-11 | [Log Redactor CLI](projects/2026-07-11-log-redactor-cli) | Sanitizes local logs by masking emails, IPv4s, UUIDs, bearer tokens, and common secret-looking keys. | `python3 -m unittest discover projects/2026-07-11-log-redactor-cli -v` |
| 2026-06-24 | [CSV Profile CLI](projects/2026-06-24-csv-profile-cli) | Summarizes CSV columns with inferred types, missing counts, distinct counts, ranges, and examples. | `python3 -m unittest discover projects/2026-06-24-csv-profile-cli -v` |
| 2026-06-24 | [Markdown Link Checker](projects/2026-06-24-markdown-link-checker) | Finds duplicate anchors, empty URLs, and malformed Markdown links in local `.md` files. | `python3 -m unittest discover projects/2026-06-24-markdown-link-checker -v` |
| 2026-06-24 | [Task Triage CLI](projects/2026-06-24-task-triage-cli) | Sorts plain-text tasks by priority, due date, and effort so the next best task is easy to pick. | `python3 -m unittest discover projects/2026-06-24-task-triage-cli -v` |
