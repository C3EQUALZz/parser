from typing import Self

from app.domain.aggregates.product_marketplace import ProductMarketPlace
from pydantic import BaseModel


class ProductMarketPlaceRequestSchema(BaseModel):
    name: str


class ProductMarketPlaceResponseSchema(BaseModel):
    product_name: str
    marketplace_name: str
    marketplace_url: str
    price: int
    link: str
    count_of_feedbacks: int
    rating: float

    @classmethod
    def from_aggregate(cls, product_marketplace: ProductMarketPlace) -> Self:
        return cls(
            product_name=product_marketplace.product.name.value,
            marketplace_name=product_marketplace.marketplace.name.value,
            marketplace_url=product_marketplace.marketplace.url.value,
            price=product_marketplace.price.value,
            link=product_marketplace.link.value,
            count_of_feedbacks=product_marketplace.count_of_feedbacks.value,
            rating=product_marketplace.rating.value,
        )
