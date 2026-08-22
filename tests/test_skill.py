from __future__ import annotations

import re
import unittest
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
SKILL_ROOT = REPO_ROOT / "link-research"


def parse_simple_mapping(path: Path) -> dict[str, str]:
    values: dict[str, str] = {}
    for raw_line in path.read_text(encoding="utf-8").splitlines():
        line = raw_line.strip()
        if not line or line.startswith("#") or line.endswith(":"):
            continue
        if ":" not in line:
            continue
        key, value = line.split(":", 1)
        values[key.strip()] = value.strip().strip('"').strip("'")
    return values


class LinkResearchSkillTests(unittest.TestCase):
    def setUp(self) -> None:
        self.skill_text = (SKILL_ROOT / "SKILL.md").read_text(encoding="utf-8")

    def test_manifest_has_discriminating_metadata(self) -> None:
        match = re.match(r"^---\n(.*?)\n---", self.skill_text, re.DOTALL)
        self.assertIsNotNone(match)
        metadata = {}
        for line in match.group(1).splitlines():
            key, value = line.split(":", 1)
            metadata[key.strip()] = value.strip()
        self.assertEqual(metadata["name"], "link-research")
        self.assertIn("user-supplied", metadata["description"])
        self.assertIn("Do not use", metadata["description"])

    def test_every_reference_link_exists(self) -> None:
        linked = set(re.findall(r"\((references/[^)]+\.md)\)", self.skill_text))
        actual = {str(path.relative_to(SKILL_ROOT)) for path in (SKILL_ROOT / "references").glob("*.md")}
        self.assertEqual(linked, actual)
        for relative in linked:
            self.assertTrue((SKILL_ROOT / relative).is_file())

    def test_ui_metadata_matches_skill(self) -> None:
        metadata = parse_simple_mapping(SKILL_ROOT / "agents" / "openai.yaml")
        self.assertIn("$link-research", metadata["default_prompt"])
        self.assertGreaterEqual(len(metadata["short_description"]), 25)
        self.assertLessEqual(len(metadata["short_description"]), 64)

    def test_no_unfinished_scaffold_content(self) -> None:
        for path in SKILL_ROOT.rglob("*"):
            if path.is_file():
                text = path.read_text(encoding="utf-8")
                self.assertNotIn("[TODO:", text, path)
                self.assertNotIn("PLACEHOLDER", text, path)


if __name__ == "__main__":
    unittest.main()
