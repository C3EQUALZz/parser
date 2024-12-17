from abc import ABC

from app.infrastructure.services.parsers.product_marketplace.wildberries.base import AbstractWildBerriesParser
from app.infrastructure.uow.product_marketplace.base import ProductsMarketPlaceUnitOfWork
from app.logic.handlers.base import (
    CT,
)
from app.logic.handlers.product_marketplace.base import ProductsMarketPlaceCommandHandler


class ProductsWildberriesPlaceCommandHandler(ProductsMarketPlaceCommandHandler[CT, AbstractWildBerriesParser], ABC):
    """
    Abstract command handler class, from which every users command handler should be inherited from.
    """

    def __init__(self, uow: ProductsMarketPlaceUnitOfWork, parser: AbstractWildBerriesParser) -> None:
        super().__init__(uow, parser)
