from abc import ABC, abstractmethod
from typing import List

from app.domain.entities.base import BaseEntity
from app.infrastructure.utils.fetchers.base import AbstractFetcher


class Parser(ABC):
    def __init__(self, fetcher: AbstractFetcher) -> None:
        self._fetcher = fetcher
        self._products = []


class MarketPlaceParser(Parser, ABC):
    @abstractmethod
    async def parse(self, key_word: str, pages_count: int) -> List[BaseEntity]:
        ...
