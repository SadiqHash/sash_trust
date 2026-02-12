"""
SashTrust - Security Validation Engine.
"""

from sash_trust.version import __version__
from sash_trust.interfaces.library.api import scan

__all__ = ["scan", "__version__"]
