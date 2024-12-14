from dataclasses import dataclass, field
from typing import List

from app.domain.aggregates.base import BaseAggregateRoot
from app.domain.entities.brand import Brand
from app.domain.entities.marketplace import Marketplace
from app.domain.entities.product import Product


@dataclass(eq=False)
class BrandMarketPlaceAggregate(BaseAggregateRoot):
    """
    Агрегат BrandMarketPlace объединяет Brand, Marketplace и связанные продукты.
    """
    brand: Brand
    marketplace: Marketplace
    external_marketplace_id: str
    products: List[Product] = field(default_factory=list)