from app.infrastructure.services.parsers.product_marketplace.wildberries.base import AbstractWildBerriesParser


class WildberriesProductService:
    """
    Service layer core according to DDD, which using a unit of work, will perform operations on the domain model.
    """
    def __init__(self, parser: AbstractWildBerriesParser) -> None:
        self._parser = parser

    async def get_all_products_with_name(self):
        ...



    async def get_all_categories(self):
        ...

