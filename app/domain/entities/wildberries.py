from dataclasses import dataclass, field

from app.domain.entities.base import BaseEntity
from app.domain.values.wildberries import Link, Article, Name, Brand, BrandId, Price, Rating, FeedBacks


@dataclass(eq=False)
class WildBerriesProduct(BaseEntity):
    """
    Domain object, which represents a Wild Berries product.
    It has several attributes:

    - **link**: link for the Wild Berries product.
    - **name**: name of the product.
    - **brand**: brand of the product.
    - **brand_id**: id of the brand of the product.
    - **price**: price of the product. Also, you can give here a discount price.
    - **rating**: rating of the product.
    - **feedbacks**: list of feedbacks related to the product.
    """
    link: Link
    article: Article
    name: Name
    brand: Brand
    brand_id: BrandId
    price: Price
    rating: Rating
    feedbacks: FeedBacks = field(default=FeedBacks(list()))

    __hash__ = BaseEntity.__hash__
    __eq__ = BaseEntity.__eq__
