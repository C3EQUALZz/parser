import json
from typing import override

from app.domain.aggregates.product_marketplace import ProductMarketPlace
from app.infrastructure.services.parsers.product_marketplace.wildberries.base import AbstractWildBerriesParser


class WildBerriesParserByArticleRequest(AbstractWildBerriesParser):
    @override
    async def parse(self, article: str) -> ProductMarketPlace:
        url = f"https://static-basket-01.wb.ru/vol0/data/main-menu-ru-ru-v2.json"
        page_source = await self._fetcher.get_page_source(url)
        page_data = json.loads(page_source)
        return page_data
