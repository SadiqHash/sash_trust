from abc import ABC, abstractmethod
from pathlib import Path
from sash_trust.core.result import Finding


class BaseValidator(ABC):

    @abstractmethod
    async def validate(self, file_path: Path) -> Finding | None:
        pass
