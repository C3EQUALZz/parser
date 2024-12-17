from abc import ABC, abstractmethod
from typing import Any

from app.infrastructure.services.parsers.base import Parser


class AbstractWildBerriesParser(Parser, ABC):
    @abstractmethod
    async def parse(self, *args, **kwargs) -> Any:
        ...
