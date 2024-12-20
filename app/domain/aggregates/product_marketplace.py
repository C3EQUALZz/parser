from dataclasses import dataclass, field
from typing import Dict, Any

from app.domain.aggregates.base import BaseAggregateRoot
from app.domain.entities.marketplace import Marketplace
from app.domain.entities.product import Product
from app.domain.values.marketplace import NameOfMarketplace, MarketPlaceUrl
from app.domain.values.product import ProductName
from app.domain.values.product_marketplace import CountOfFeedBacks, Rating, Link, Price


@dataclass(eq=False)
class ProductMarketPlace(BaseAggregateRoot):
    """
    Агрегат для хранения цены продукта на конкретном маркетплейсе.
    """
    product: Product
    marketplace: Marketplace
    price: Price
    link: Link
    count_of_feedbacks: CountOfFeedBacks = field(default=CountOfFeedBacks(0), kw_only=True)
    rating: Rating = field(default=Rating(0), kw_only=True)

    @classmethod
    def from_wildberries_json(cls, item: Dict[str, Any]) -> 'ProductMarketPlace':
        price = Price(
            int(item['salePriceU'] / 100)
            if item.get('salePriceU') is not None
            else int(item['priceU'] / 100)
        )

        name_market_place = NameOfMarketplace("wildberries")
        url_market_place = MarketPlaceUrl("https://www.wildberries.ru")

        return cls(
            product=Product(ProductName(item.get('name', ""))),
            marketplace=Marketplace(name=name_market_place, url=url_market_place),
            price=price,
            link=Link(f"https://www.wildberries.ru/catalog/{item.get('id')}/detail.aspx"),
            count_of_feedbacks=CountOfFeedBacks(item.get('feedbacks', 0)),
            rating=Rating(item.get("rating", 0)),
        )
