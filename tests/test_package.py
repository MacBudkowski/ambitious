from pathlib import Path
import json
import unittest

ROOT = Path(__file__).resolve().parents[1]

class PackageTests(unittest.TestCase):
    def test_required_files(self):
        for name in ("SKILL.md", "README.md", "LICENSE", "examples.md", "evals/scenarios.json"):
            self.assertTrue((ROOT / name).is_file(), name)

    def test_skill_contract(self):
        text = (ROOT / "SKILL.md").read_text()
        self.assertTrue(text.startswith("---\n"))
        front, body = text[4:].split("\n---\n", 1)
        for key in ("name:", "description:", "version:", "author:", "license:"):
            self.assertIn(key, front)
        self.assertIn("name: ambition-check", front)
        for term in ("**Speed:**", "**Depth:**", "**Range:**", "**Altitude:**", "Wait for approval", "Stop and let the user react", "at most two", "permanent favorite"):
            self.assertIn(term, body)

    def test_scenario_coverage(self):
        cases = json.loads((ROOT / "evals/scenarios.json").read_text())
        ids = [c["id"] for c in cases]
        self.assertEqual(len(ids), len(set(ids)))
        self.assertTrue(set(("speed", "depth", "range", "altitude", "narrow", "urgent", "declined", "uncertain", "permission", "two-directions")).issubset(ids))
        for case in cases:
            self.assertTrue(case["prompt"])
            self.assertGreaterEqual(len(case["pass_criteria"]), 2)

    def test_no_machine_specific_content(self):
        for path in ROOT.rglob("*"):
            if path.is_file() and path.suffix in (".md", ".json"):
                text = path.read_text()
                for forbidden in ("/Users/", "/home/", "wallfacer"):
                    self.assertNotIn(forbidden, text, str(path))

    def test_license_and_evaluation_disclosure(self):
        self.assertIn("MIT License", (ROOT / "LICENSE").read_text())
        self.assertIn("not model behavior", (ROOT / "README.md").read_text())

if __name__ == "__main__":
    unittest.main()
