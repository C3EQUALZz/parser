from abc import ABC

from app.infrastructure.uow.product_marketplace.base import ProductsMarketPlaceUnitOfWork
from app.logic.handlers.base import (
    AbstractCommandHandler,
    AbstractEventHandler,
    CT,
    ET,
)


class ProductsMarketPlaceEventHandler(AbstractEventHandler[ET], ABC):
    """
    Abstract event handler class, from which every users event handler should be inherited from.
    """

    def __init__(self, uow: ProductsMarketPlaceUnitOfWork) -> None:
        self._uow: ProductsMarketPlaceUnitOfWork = uow


class ProductsMarketPlaceCommandHandler(AbstractCommandHandler[CT], ABC):
    """
    Abstract command handler class, from which every users command handler should be inherited from.
    """

    def __init__(self, uow: ProductsMarketPlaceUnitOfWork) -> None:
        self._uow: ProductsMarketPlaceUnitOfWork = uow
