from typing import List

from app.domain.aggregates.product_marketplace import ProductMarketPlace
from app.infrastructure.services.parsers.product_marketplace.wildberries.base import AbstractWildBerriesParser


class WildberriesService:
    """
    Service layer core according to DDD, which using a unit of work, will perform operations on the domain model.
    """

    def __init__(self, parser: AbstractWildBerriesParser) -> None:
        self._parser = parser

    async def get_products_with_name(self, name: str) -> List[ProductMarketPlace]:
        return await self._parser.parse(name=name)

    async def get_products_by_category(self, category: str) -> List[ProductMarketPlace]:
        return await self._parser.parse(category=category)

    async def get_product_by_article(self, article: str) -> ProductMarketPlace:
        return await self._parser.parse(article=article)

    async def get_popular_products(self) -> List[ProductMarketPlace]:
        return await self._parser.parse()

    async def get_all_categories(self):
        """
        Get all categories from
        :return:
        """
        return await self._parser.parse()
