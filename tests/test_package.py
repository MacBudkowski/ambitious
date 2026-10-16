"""Structural checks for the ambitious package (stdlib only).

These verify packaging, not model behavior.
"""
from __future__ import annotations

import hashlib
import json
import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PILLARS = ("speed", "depth", "range", "altitude")

# SHA-256 of each verbatim block. Update only if the quoted source text is
# intentionally changed (e.g. replaced by a link for public redistribution).
VERBATIM_SHA256 = {
    "speed": "d8ba467ec5c9e63c2c19c372319e7f7e57120d5edc36651bdd76c576ead2a6ff",
    "depth": "80689ca92cab76efdeec01e7504f7e157703cbc282db0892bcccd19a64c6ee27",
    "range": "0f6b0d42e08d0d857a30f45f6883e1162ee0f1e8045b2c7565901d64c677cc0a",
    "altitude": "d9ff36e1357770da77e7921b11262f9312128942f853beb6cf7d6b616e3549f4",
}


def frontmatter(text: str) -> dict:
    assert text.startswith("---\n"), "frontmatter must start at byte 0"
    head, _ = text[4:].split("\n---\n", 1)
    out = {}
    for line in head.splitlines():
        m = re.match(r"^([a-z_]+):\s*(.*)$", line)
        if m:
            out[m.group(1)] = m.group(2).strip().strip('"')
    return out


def verbatim_block(text: str) -> str:
    m = re.search(r"--- BEGIN VERBATIM ---\n\n(.*)\n\n--- END VERBATIM ---", text, re.S)
    assert m, "verbatim block missing"
    return m.group(1)


class PackageTests(unittest.TestCase):
    def test_required_files(self):
        for name in ["SKILL.md", "README.md", "LICENSE", "CHANGELOG.md",
                     "references/examples.md", "references/source-notice.md", "references/precedents.md",
                     *[f"references/{p}.md" for p in PILLARS]]:
            self.assertTrue((ROOT / name).is_file(), name)

    def test_frontmatter(self):
        """Follows the open Agent Skills spec (agentskills.io/specification)."""
        text = (ROOT / "SKILL.md").read_text()
        fm = frontmatter(text)
        name = fm.get("name", "")
        self.assertEqual(name, "ambitious")
        self.assertRegex(name, r"^[a-z0-9]+(-[a-z0-9]+)*$")
        self.assertLessEqual(len(name), 64)
        desc = fm.get("description", "")
        self.assertTrue(desc.startswith("Use when"), "description should lead with the trigger")
        self.assertLessEqual(len(desc), 1024)
        first_sentence = desc.split(". ")[0]
        self.assertLessEqual(len(first_sentence), 60, "some hosts truncate descriptions; keep the trigger first and short")
        head = text[4:text.index("\n---\n", 4)]
        for key in ("author:", "version:"):
            self.assertIn(key, head)

    def test_host_neutral(self):
        """The skill itself must not assume a particular agent host."""
        for path in [ROOT / "SKILL.md", ROOT / "README.md", *(ROOT / "references").glob("*.md")]:
            text = path.read_text().lower()
            for host in ("hermes",):
                self.assertNotIn(host, text, f"{path.name} mentions {host}")

    def test_skill_is_concise(self):
        text = (ROOT / "SKILL.md").read_text()
        body = text[text.index("\n---\n", 4) + 5:]
        words = len(body.split())
        self.assertLess(words, 1500, f"SKILL.md has {words} words; move detail to references/")

    def test_skill_names_every_pillar_and_links_resolve(self):
        text = (ROOT / "SKILL.md").read_text()
        for p in PILLARS:
            self.assertIn(f"**{p.capitalize()}**", text)
            self.assertIn(f"references/{p}.md", text)
        for md in [ROOT / "SKILL.md", ROOT / "README.md", *(ROOT / "references").glob("*.md")]:
            for link in re.findall(r"\]\(([^)#]+)(?:#[^)]*)?\)", md.read_text()):
                if link.startswith(("http://", "https://", "mailto:")):
                    continue
                self.assertTrue((md.parent / link).exists(), f"{md.name}: broken link {link}")

    def test_reference_structure(self):
        for p in PILLARS:
            text = (ROOT / "references" / f"{p}.md").read_text()
            for section in ("## How to build the ladder", "## Common mistakes", "## What the article says"):
                self.assertIn(section, text, f"{p}.md missing {section}")
            self.assertIn("felixrieseberg.com", text)
            self.assertIn("source-notice.md", text)

    def test_verbatim_quotes_unchanged(self):
        for p in PILLARS:
            block = verbatim_block((ROOT / "references" / f"{p}.md").read_text())
            digest = hashlib.sha256(block.encode()).hexdigest()
            expected = VERBATIM_SHA256[p]
            if expected:
                self.assertEqual(digest, expected, f"verbatim text in {p}.md changed")
            first = block.split("\n", 1)[0]
            if p != "speed":
                self.assertEqual(first, p.capitalize(), f"{p}.md quotes the wrong section")

    def test_no_machine_specific_content(self):
        for path in ROOT.rglob("*"):
            if ".git" in path.parts or "results" in path.parts or not path.is_file():
                continue
            if path.suffix in (".md", ".json", ".py"):
                text = path.read_text()
                for bad in ("/" + "Users/", "/" + "home/", "wall" + "facer"):
                    self.assertNotIn(bad, text, f"{path.relative_to(ROOT)} contains {bad}")

    def test_license(self):
        self.assertIn("MIT License", (ROOT / "LICENSE").read_text())


if __name__ == "__main__":
    unittest.main()
