from dataclasses import dataclass
from typing import List


@dataclass(frozen=True)
class Finding:
    file_path: str
    message: str
    severity: int


@dataclass(frozen=True)
class ScanResult:
    findings: List[Finding]
    trust_score: float
