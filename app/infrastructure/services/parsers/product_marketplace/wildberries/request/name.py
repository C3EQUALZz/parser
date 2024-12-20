import json
from typing import List

from typing_extensions import override

from app.domain.aggregates.product_marketplace import ProductMarketPlace
from app.infrastructure.services.parsers.product_marketplace.wildberries.base import AbstractWildBerriesParser


class WildBerriesParserByNameRequest(AbstractWildBerriesParser):
    @override
    async def parse(self, name: str, pages_count: int = 3) -> List[ProductMarketPlace]:
        products = []

        for page in range(1, pages_count + 1):
            url = (f"https://search.wb.ru/exactmatch/ru/common/v4/search?"
                   f"appType=1&curr=rub&dest=-1257786&page={page}"
                   f"&query={'%20'.join(name.split())}&resultset=catalog"
                   f"&sort=popular&spp=24&suppressSpellcheck=false")
            products.extend(await self.__get_products(url=url))

        return products

    async def __get_products(self, url: str) -> List[ProductMarketPlace]:
        products_on_page: List[ProductMarketPlace] = []

        page_data = json.loads(await self._fetcher.get_page_source(url=url))

        if page_data.get("data") is None or page_data.get("data").get("products") is None:
            return products_on_page

        for item in page_data.get("data").get("products"):
            products_on_page.append(ProductMarketPlace.from_wildberries_json(item))

        return products_on_page
