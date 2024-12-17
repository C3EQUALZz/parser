from typing import List

from app.domain.aggregates.product_marketplace import ProductMarketPlace
from app.infrastructure.services.wildberries import WildberriesService
from app.logic.commands.product_marketplace.wildberries import ParseAllProductsFromACertainNumberOfPagesWithKeyName
from app.logic.handlers.product_marketplace.wildberries.base import ProductsWildberriesPlaceCommandHandler


class ParseAllProductsFromACertainNumberOfPagesWithKeyNameCommandHandler(
    ProductsWildberriesPlaceCommandHandler[ParseAllProductsFromACertainNumberOfPagesWithKeyName]
):
    async def __call__(self, command: ParseAllProductsFromACertainNumberOfPagesWithKeyName) -> List[ProductMarketPlace]:
        wildberries_service: WildberriesService = WildberriesService(self._parser)
        return await wildberries_service.get_products_with_name(name=command.key_word)


