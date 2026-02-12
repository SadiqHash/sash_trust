import json
from pathlib import Path
from typing import Any

import yaml

from sash_trust.policy.schema import PolicySchema


class PolicyLoader:

    @staticmethod
    def load(path: Path) -> PolicySchema:
        if not path.exists():
            raise FileNotFoundError("Policy file not found")

        if path.suffix in [".yaml", ".yml"]:
            data = yaml.safe_load(path.read_text())
        elif path.suffix == ".json":
            data = json.loads(path.read_text())
        else:
            raise ValueError("Unsupported policy format")

        return PolicySchema.model_validate(data)
