PYTHON ?= python3

.PHONY: verify
verify:
	$(PYTHON) -B -m unittest discover -s projects/2026-06-24-markdown-link-checker -v
	$(PYTHON) -B -m unittest discover -s projects/2026-06-24-task-triage-cli -v
	$(PYTHON) -B -m unittest discover -s projects/2026-07-20-csv-schema-drift-detector -v
	$(PYTHON) -B -m unittest discover -s projects/2026-07-21-env-contract-checker -v
	$(PYTHON) -B -m unittest discover -s projects/2026-07-23-jsonl-auditor -v
.PHONY: lint security check
lint:
	$(PYTHON) -m ruff check --config ruff.toml --no-cache .

security:
	$(PYTHON) -m bandit -q -ll -ii -r . -x ./.venv,./.git

check: verify lint security
