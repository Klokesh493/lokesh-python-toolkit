PYTHON ?= python3

.PHONY: verify
verify:
	$(PYTHON) -B -m unittest discover -s projects/2026-06-24-markdown-link-checker -v
	$(PYTHON) -B -m unittest discover -s projects/2026-06-24-task-triage-cli -v
	$(PYTHON) -B -m unittest discover -s projects/2026-07-20-csv-schema-drift-detector -v
	$(PYTHON) -B -m unittest discover -s projects/2026-07-21-env-contract-checker -v
	$(PYTHON) -B -m unittest discover -s projects/2026-07-23-jsonl-auditor -v
