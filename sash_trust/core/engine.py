from __future__ import annotations

from pathlib import Path
from typing import Iterable

from sash_trust.core.scanner import FileScanner
from sash_trust.core.scoring import TrustScorer
from sash_trust.core.result import ScanResult
from sash_trust.policy.loader import PolicyLoader
from sash_trust.validators.base import BaseValidator


class SashTrustEngine:
    """
    Core scanning engine.
    Language-agnostic orchestration layer.
    """

    def __init__(self, policy_path: Path):
        self._policy = PolicyLoader.load(policy_path)
        self._scanner = FileScanner()
        self._scorer = TrustScorer()

    async def scan(self, target: Path) -> ScanResult:
        files = list(self._scanner.scan(target))
        validators: Iterable[BaseValidator] = self._policy.build_validators()

        findings = []

        for file in files:
            for validator in validators:
                result = await validator.validate(file)
                if result:
                    findings.append(result)

        score = self._scorer.calculate(findings)

        return ScanResult(
            findings=findings,
            trust_score=score,
        )
