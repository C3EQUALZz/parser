from dataclasses import dataclass, field

from app.domain.aggregates.base import BaseAggregateRoot
from app.domain.entities.marketplace import Marketplace
from app.domain.entities.product import Product
from app.domain.values.product_marketplace import FeedBacks, Rating, Link, Price


@dataclass(eq=False)
class ProductMarketPlace(BaseAggregateRoot):
    """
    Агрегат для хранения цены продукта на конкретном маркетплейсе.
    """
    product: Product
    marketplace: Marketplace
    price: Price
    link: Link
    feedbacks: FeedBacks = field(default=FeedBacks(list()), kw_only=True)
    rating: Rating = field(default=Rating(0), kw_only=True)
