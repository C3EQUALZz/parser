from abc import (
    ABC,
    abstractmethod,
)
from typing import (
    List,
    Optional,
)

from app.domain.entities.wildberries import WildBerriesProduct
from app.infrastructure.repositories.base import AbstractRepository


class WildBerriesProductsRepository(AbstractRepository[WildBerriesProduct], ABC):
    """
    An interface for work with WildBerries products, that is used by books unit of work.
    The main goal is that implementations of this interface can be easily replaced in users unit of work
    using dependency injection without disrupting its functionality.
    """

    @abstractmethod
    async def get_by_link(self, link: str) -> Optional[WildBerriesProduct]:
        raise NotImplementedError

    @abstractmethod
    async def get_by_article(self, article: int) -> Optional[WildBerriesProduct]:
        raise NotImplementedError

    @abstractmethod
    async def add(self, model: WildBerriesProduct) -> WildBerriesProduct:
        raise NotImplementedError

    @abstractmethod
    async def get(self, article: int) -> Optional[WildBerriesProduct]:
        raise NotImplementedError

    @abstractmethod
    async def update(self, article: int, model: WildBerriesProduct) -> WildBerriesProduct:
        raise NotImplementedError

    @abstractmethod
    async def delete(self, article: int) -> None:
        raise NotImplementedError

    @abstractmethod
    def list(self) -> List[WildBerriesProduct]:
        raise NotImplementedError
