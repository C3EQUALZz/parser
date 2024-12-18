from typing import override, List

from app.domain.aggregates.product_marketplace import ProductMarketPlace
from app.infrastructure.services.parsers.product_marketplace.wildberries.base import AbstractWildBerriesParser


class WildBerriesParserByBrandRequest(AbstractWildBerriesParser):
    @override
    async def parse(self, brand: str, count_of_elements: int = 3) -> List[ProductMarketPlace]:
        products = []

        current_index_element = 0

        while current_index_element < count_of_elements:
            ...
