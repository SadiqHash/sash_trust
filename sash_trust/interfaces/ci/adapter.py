from sash_trust.core.result import ScanResult


def evaluate(result: ScanResult, threshold: float = 80.0) -> int:
    return 0 if result.trust_score >= threshold else 1
