import io
import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

from jsonl_auditor import audit


PROJECT_DIR = Path(__file__).parent


class AuditTests(unittest.TestCase):
    def test_clean_records_report_shapes(self):
        report = audit(io.StringIO('{"id": 1, "name": "Ada"}\n{"id": 2, "name": "Lin"}\n'))

        self.assertEqual(report["records"], 2)
        self.assertEqual(report["issues"], 0)
        self.assertEqual(
            report["shapes"], [{"fields": ["id", "name"], "count": 2}]
        )

    def test_reports_each_supported_problem(self):
        source = (
            '{"key": "a", "value": 1}\n'
            "\n"
            '{"key": "a", "value": 2}\n'
            "[1, 2]\n"
            '{"broken": }\n'
        )
        report = audit(io.StringIO(source), id_field="key")

        self.assertEqual(report["issues"], 4)
        self.assertEqual(report["blank_lines"], [2])
        self.assertEqual(report["non_object_lines"], [4])
        self.assertEqual(report["malformed"][0]["line"], 5)
        self.assertEqual(
            report["duplicate_ids"],
            [{"value": "a", "first_line": 1, "line": 3}],
        )

    def test_cli_exit_codes_and_output(self):
        with tempfile.TemporaryDirectory() as directory:
            clean = Path(directory) / "clean.jsonl"
            clean.write_text('{"id": 1}\n', encoding="utf-8")
            result = subprocess.run(
                [sys.executable, PROJECT_DIR / "jsonl_auditor.py", clean],
                capture_output=True,
                text=True,
                check=False,
            )

        self.assertEqual(result.returncode, 0)
        self.assertEqual(json.loads(result.stdout)["records"], 1)

    def test_cli_returns_one_for_issues(self):
        with tempfile.TemporaryDirectory() as directory:
            bad = Path(directory) / "bad.jsonl"
            bad.write_text('{"id": 1}\n{"id": 1}\n', encoding="utf-8")
            result = subprocess.run(
                [sys.executable, PROJECT_DIR / "jsonl_auditor.py", bad],
                capture_output=True,
                text=True,
                check=False,
            )

        self.assertEqual(result.returncode, 1)
        self.assertEqual(json.loads(result.stdout)["issues"], 1)


if __name__ == "__main__":
    unittest.main()
