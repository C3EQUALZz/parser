from abc import (
    ABC,
    abstractmethod,
)
from typing import (
    List,
    Optional,
)

from app.domain.aggregates.product_marketplace import ProductMarketPlace
from app.domain.entities.marketplace import Marketplace
from app.domain.entities.product import Product
from app.infrastructure.repositories.base import AbstractRepository


class ProductMarketPlaceRepository(AbstractRepository[ProductMarketPlace], ABC):
    """
    An interface for work with WildBerries products, that is used by books unit of work.
    The main goal is that implementations of this interface can be easily replaced in users unit of work
    using dependency injection without disrupting its functionality.
    """

    @abstractmethod
    async def get_by_link(self, link: str) -> Optional[ProductMarketPlace]:
        raise NotImplementedError

    @abstractmethod
    async def get_by_product_and_marketplace(
            self,
            product: Product,
            market_place: Marketplace
    ) -> Optional[ProductMarketPlace]:
        raise NotImplementedError

    @abstractmethod
    async def add(self, model: ProductMarketPlace) -> ProductMarketPlace:
        raise NotImplementedError

    @abstractmethod
    async def get(self, oid: str) -> Optional[ProductMarketPlace]:
        raise NotImplementedError

    @abstractmethod
    async def update(self, oid: str, model: ProductMarketPlace) -> ProductMarketPlace:
        raise NotImplementedError

    @abstractmethod
    async def delete(self, oid: str) -> None:
        raise NotImplementedError

    @abstractmethod
    async def list(self) -> List[ProductMarketPlace]:
        raise NotImplementedError
