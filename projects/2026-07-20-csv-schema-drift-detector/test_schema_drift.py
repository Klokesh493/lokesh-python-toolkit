import tempfile
import unittest
from pathlib import Path

from schema_drift import compare, value_type


class SchemaDriftTests(unittest.TestCase):
    def test_value_type_order_avoids_boolean_and_integer_confusion(self):
        self.assertEqual(value_type("false"), "boolean")
        self.assertEqual(value_type("12"), "integer")
        self.assertEqual(value_type("12.5"), "number")
        self.assertEqual(value_type(""), "empty")

    def test_reports_columns_and_type_changes(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            baseline = root / "baseline.csv"
            candidate = root / "candidate.csv"
            baseline.write_text("id,name,active\n1,Ada,true\n2,Lin,false\n", encoding="utf-8")
            candidate.write_text("id,name,score\nA1,Ada,9.5\nA2,Lin,8\n", encoding="utf-8")

            result = compare(baseline, candidate)

        self.assertEqual(result["added_columns"], ["score"])
        self.assertEqual(result["removed_columns"], ["active"])
        self.assertEqual(
            result["changed_types"]["id"],
            {"baseline": ["integer"], "candidate": ["text"]},
        )
        self.assertTrue(result["drift_detected"])

    def test_empty_values_do_not_create_false_type_drift(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            baseline = root / "baseline.csv"
            candidate = root / "candidate.csv"
            baseline.write_text("id,note\n1,ready\n2,\n", encoding="utf-8")
            candidate.write_text("id,note\n3,\n4,done\n", encoding="utf-8")
            self.assertFalse(compare(baseline, candidate)["drift_detected"])


if __name__ == "__main__":
    unittest.main()
