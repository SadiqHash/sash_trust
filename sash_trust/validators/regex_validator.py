import re
from pathlib import Path
from sash_trust.validators.base import BaseValidator
from sash_trust.core.result import Finding


class RegexValidator(BaseValidator):

    def __init__(self, pattern: str, severity: int):
        self._regex = re.compile(pattern)
        self._severity = severity

    async def validate(self, file_path: Path):
        try:
            content = file_path.read_text(errors="ignore")
        except Exception:
            return None

        if self._regex.search(content):
            return Finding(
                file_path=str(file_path),
                message="Regex pattern matched",
                severity=self._severity,
            )
        return None
