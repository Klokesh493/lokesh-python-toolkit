# Local verification

Command: `make verify`

Result: **PASS**

````text
python3 -B -m unittest discover -s projects/2026-06-24-markdown-link-checker -v
python3 -B -m unittest discover -s projects/2026-06-24-task-triage-cli -v
python3 -B -m unittest discover -s projects/2026-07-20-csv-schema-drift-detector -v
python3 -B -m unittest discover -s projects/2026-07-21-env-contract-checker -v
python3 -B -m unittest discover -s projects/2026-07-23-jsonl-auditor -v
test_reports_duplicate_anchors (test_markdown_link_checker.MarkdownLinkCheckerTests) ... ok
test_reports_empty_label_and_target (test_markdown_link_checker.MarkdownLinkCheckerTests) ... ok
test_reports_missing_local_anchor (test_markdown_link_checker.MarkdownLinkCheckerTests) ... ok
test_scan_paths_reports_missing_file (test_markdown_link_checker.MarkdownLinkCheckerTests) ... ok
test_slugifies_heading_text (test_markdown_link_checker.MarkdownLinkCheckerTests) ... ok

----------------------------------------------------------------------
Ran 5 tests in 0.001s

OK
test_invalid_priority_reports_line_number (test_task_triage.TaskTriageTests) ... ok
test_json_serializer_uses_iso_date (test_task_triage.TaskTriageTests) ... ok
test_load_tasks_sorts_high_value_work_first (test_task_triage.TaskTriageTests) ... ok
test_parse_relative_due_dates (test_task_triage.TaskTriageTests) ... ok

----------------------------------------------------------------------
Ran 4 tests in 0.000s

OK
test_empty_values_do_not_create_false_type_drift (test_schema_drift.SchemaDriftTests) ... ok
test_reports_columns_and_type_changes (test_schema_drift.SchemaDriftTests) ... ok
test_value_type_order_avoids_boolean_and_integer_confusion (test_schema_drift.SchemaDriftTests) ... ok

----------------------------------------------------------------------
Ran 3 tests in 0.002s

OK
test_cli_strict_mode_fails_on_warning (test_env_contract.EnvContractTests) ... ok
test_matching_contract_has_no_findings (test_env_contract.EnvContractTests) ... ok
test_parser_accepts_comments_export_and_quoted_spaces (test_env_contract.EnvContractTests) ... ok
test_reports_contract_and_syntax_problems_without_values (test_env_contract.EnvContractTests) ... ok

----------------------------------------------------------------------
Ran 4 tests in 0.035s

OK
test_clean_records_report_shapes (test_jsonl_auditor.AuditTests) ... ok
test_cli_exit_codes_and_output (test_jsonl_auditor.AuditTests) ... ok
test_cli_returns_one_for_issues (test_jsonl_auditor.AuditTests) ... ok
test_reports_each_supported_problem (test_jsonl_auditor.AuditTests) ... ok

----------------------------------------------------------------------
Ran 4 tests in 0.059s

OK
````
