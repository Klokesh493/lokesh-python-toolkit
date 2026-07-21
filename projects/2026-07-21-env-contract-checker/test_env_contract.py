import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

from env_contract import check_contract, parse_env


class EnvContractTests(unittest.TestCase):
    def write(self, directory: str, name: str, content: str) -> Path:
        path = Path(directory, name)
        path.write_text(content, encoding="utf-8")
        return path

    def test_matching_contract_has_no_findings(self):
        with tempfile.TemporaryDirectory() as directory:
            example = self.write(directory, "example", "API_URL=\nTOKEN=\n")
            actual = self.write(directory, "actual", "TOKEN=secret\nAPI_URL=https://example.test\n")
            self.assertEqual(check_contract(example, actual), [])

    def test_reports_contract_and_syntax_problems_without_values(self):
        with tempfile.TemporaryDirectory() as directory:
            example = self.write(directory, "example", "API_URL=\nTOKEN=\n")
            actual = self.write(directory, "actual", "API_URL=hello world\nEXTRA=hidden-value\nEXTRA=other\n")
            findings = check_contract(example, actual)
            self.assertEqual(
                {finding.code for finding in findings},
                {"unquoted-space", "duplicate", "missing", "extra"},
            )
            self.assertNotIn("hidden-value", " ".join(f.message for f in findings))

    def test_parser_accepts_comments_export_and_quoted_spaces(self):
        with tempfile.TemporaryDirectory() as directory:
            path = self.write(directory, "env", "# comment\nexport GOOD_KEY='two words'\nEMPTY=\n")
            keys, findings = parse_env(path)
            self.assertEqual(keys, {"GOOD_KEY", "EMPTY"})
            self.assertEqual(findings, [])

    def test_cli_strict_mode_fails_on_warning(self):
        with tempfile.TemporaryDirectory() as directory:
            example = self.write(directory, "example", "ONE=\n")
            actual = self.write(directory, "actual", "ONE=yes\nTWO=yes\n")
            result = subprocess.run(
                [sys.executable, str(Path(__file__).with_name("env_contract.py")), str(example), str(actual), "--strict"],
                capture_output=True,
                text=True,
                check=False,
            )
            self.assertEqual(result.returncode, 1)
            self.assertIn("WARNING [extra] unexpected key TWO", result.stdout)


if __name__ == "__main__":
    unittest.main()
