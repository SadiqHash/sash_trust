import math
from pathlib import Path
from sash_trust.validators.base import BaseValidator
from sash_trust.core.result import Finding


class EntropyValidator(BaseValidator):

    def __init__(self, threshold: float = 4.5):
        self._threshold = threshold

    def _entropy(self, data: str) -> float:
        probabilities = [float(data.count(c)) / len(data) for c in set(data)]
        return -sum(p * math.log2(p) for p in probabilities)

    async def validate(self, file_path: Path):
        try:
            content = file_path.read_text(errors="ignore")
        except Exception:
            return None

        if not content:
            return None

        if self._entropy(content) > self._threshold:
            return Finding(
                file_path=str(file_path),
                message="High entropy detected",
                severity=10,
            )

        return None
