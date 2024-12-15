from typing import Optional, override, List, Sequence, Any

from sqlalchemy import Result, select, update, delete, RowMapping, Row

from app.domain.aggregates.product_marketplace import ProductMarketPlace
from app.domain.entities.marketplace import Marketplace
from app.domain.entities.product import Product
from app.infrastructure.repositories.base import SQLAlchemyAbstractRepository
from app.infrastructure.repositories.product_marketplace.base import ProductMarketPlaceRepository


class SQLAlchemyProductMarketPlaceRepository(
    SQLAlchemyAbstractRepository[ProductMarketPlace],
    ProductMarketPlaceRepository
):

    @override
    async def get_by_link(self, link: str) -> Optional[ProductMarketPlace]:
        ...

    @override
    async def get_by_product_and_marketplace(
            self,
            product: Product,
            market_place: Marketplace
    ) -> Optional[ProductMarketPlace]:
        ...

    @override
    async def add(self, model: ProductMarketPlace) -> ProductMarketPlace:
        ...

    @override
    async def get(self, oid: str) -> Optional[ProductMarketPlace]:
        result: Result = await self._session.execute(select(ProductMarketPlace).filter_by(oid=oid))
        return result.scalar_one_or_none()

    @override
    async def update(self, oid: str, model: ProductMarketPlace) -> ProductMarketPlace:
        result: Result = await self._session.execute(
            update(ProductMarketPlace)
            .filter_by(oid=oid)
            .values(**await model.to_dict(exclude={'oid'}))
            .returning(ProductMarketPlace)
        )

        return result.scalar_one()

    @override
    async def delete(self, oid: str) -> None:
        await self._session.execute(delete(ProductMarketPlace).filter_by(oid=oid))

    @override
    async def list(self) -> List[ProductMarketPlace]:
        result: Result = await self._session.execute(select(ProductMarketPlace))
        users: Sequence[Row | RowMapping | Any] = result.scalars().all()

        assert isinstance(users, List)
        for user in users:
            assert isinstance(user, ProductMarketPlace)

        return users
