from dataclasses import dataclass

from app.domain.entities.base import BaseEntity
from app.domain.values.product import ProductName


@dataclass(eq=False)
class Product(BaseEntity):
    name: ProductName

    __hash__ = BaseEntity.__hash__
    __eq__ = BaseEntity.__eq__
