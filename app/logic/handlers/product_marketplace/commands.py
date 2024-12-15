from typing import List

from app.domain.aggregates.product_marketplace import ProductMarketPlace
from app.logic.commands.product_marketplace import ParseAllProductsFromACertainNumberOfPagesWithKeyName
from app.logic.handlers.product_marketplace.base import ProductsMarketPlaceCommandHandler


class ParseAllProductsFromACertainNumberOfPagesWithKeyNameCommandHandler(
    ProductsMarketPlaceCommandHandler[ParseAllProductsFromACertainNumberOfPagesWithKeyName]
):
    async def __call__(self, command: ParseAllProductsFromACertainNumberOfPagesWithKeyName) -> List[ProductMarketPlace]:
        ...


