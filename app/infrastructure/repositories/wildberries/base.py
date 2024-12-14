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
    def get_by_title(self, title: str) -> Optional[WildBerriesProduct]:
        raise NotImplementedError

    @abstractmethod
    def get_by_title_and_author(self, title: str, author: str) -> Optional[WildBerriesProduct]:
        raise NotImplementedError

    @abstractmethod
    def add(self, model: WildBerriesProduct) -> WildBerriesProduct:
        raise NotImplementedError

    @abstractmethod
    def get(self, oid: str) -> Optional[WildBerriesProduct]:
        raise NotImplementedError

    @abstractmethod
    def update(self, oid: str, model: WildBerriesProduct) -> WildBerriesProduct:
        raise NotImplementedError

    @abstractmethod
    def delete(self, oid: str) -> None:
        raise NotImplementedError

    @abstractmethod
    def list(self) -> List[WildBerriesProduct]:
        raise NotImplementedError
