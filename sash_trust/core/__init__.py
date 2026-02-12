"""
Core engine module.
Pure orchestration logic.
"""

from .engine import SashTrustEngine
from .result import ScanResult, Finding

__all__ = ["SashTrustEngine", "ScanResult", "Finding"]
