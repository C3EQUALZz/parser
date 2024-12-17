from abc import ABC
from typing import TypeVar, Generic

from app.infrastructure.services.parsers.base import Parser
from app.infrastructure.uow.product_marketplace.base import ProductsMarketPlaceUnitOfWork
from app.logic.handlers.base import (
    AbstractCommandHandler,
    AbstractEventHandler,
    CT,
    ET,
)

P = TypeVar("P", bound=Parser)


class ProductsMarketPlaceEventHandler(AbstractEventHandler[ET], ABC):
    """
    Abstract event handler class, from which every users event handler should be inherited from.
    """

    def __init__(self, uow: ProductsMarketPlaceUnitOfWork) -> None:
        self._uow: ProductsMarketPlaceUnitOfWork = uow


class ProductsMarketPlaceCommandHandler(AbstractCommandHandler[CT], ABC, Generic[CT, P]):
    """
    Abstract command handler class, from which every users command handler should be inherited from.
    """

    def __init__(self, uow: ProductsMarketPlaceUnitOfWork, parser: P) -> None:
        self._uow: ProductsMarketPlaceUnitOfWork = uow
        self._parser: P = parser
