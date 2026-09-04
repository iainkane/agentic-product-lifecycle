import subprocess
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


class RepositoryValidationTest(unittest.TestCase):
    def test_repository_validation(self) -> None:
        result = subprocess.run(
            [sys.executable, str(ROOT / "scripts" / "validate.py")],
            cwd=ROOT,
            check=False,
            capture_output=True,
            text=True,
        )
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)


if __name__ == "__main__":
    unittest.main()
