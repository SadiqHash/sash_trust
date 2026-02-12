from typing import List
from sash_trust.core.result import Finding


class TrustScorer:
    """
    Calculates trust score.
    """

    def calculate(self, findings: List[Finding]) -> float:
        if not findings:
            return 100.0

        penalty = sum(f.severity for f in findings)
        score = max(0.0, 100.0 - penalty)
        return round(score, 2)
