import asyncio
from pathlib import Path
from sash_trust.core.engine import SashTrustEngine


def scan(target: str, policy: str):
    engine = SashTrustEngine(Path(policy))
    return asyncio.run(engine.scan(Path(target)))
