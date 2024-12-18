from typing import List

from app.domain.aggregates.product_marketplace import ProductMarketPlace
from app.infrastructure.services.parsers.product_marketplace.wildberries.base import AbstractWildBerriesParser
from app.infrastructure.services.wildberries import WildberriesService


class WildberriesView:
    def __init__(self, parser: AbstractWildBerriesParser):
        self._parser: AbstractWildBerriesParser = parser

    async def get_products_by_name(self, name: str) -> List[ProductMarketPlace]:
        wildberries_service: WildberriesService = WildberriesService(self._parser)
        products: List[ProductMarketPlace] = await wildberries_service.get_products_with_name(name)
        return products
