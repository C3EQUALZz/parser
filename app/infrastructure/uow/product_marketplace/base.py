from abc import ABC

from app.infrastructure.repositories.product_marketplace.base import ProductMarketPlaceRepository
from app.infrastructure.uow.base import AbstractUnitOfWork


class ProductsMarketUnitOfWork(AbstractUnitOfWork, ABC):
    """
    An interface for work with books, that is used by service layer of books module.
    The main goal is that implementations of this interface can be easily replaced in the service layer
    using dependency injection without disrupting its functionality.
    """

    products_market: ProductMarketPlaceRepository
