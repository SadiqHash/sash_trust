from pathlib import Path
from typing import Generator


class FileScanner:
    """
    Safe recursive file traversal.
    """

    def scan(self, root: Path) -> Generator[Path, None, None]:
        if not root.exists():
            return

        for path in root.rglob("*"):
            if path.is_file():
                yield path
