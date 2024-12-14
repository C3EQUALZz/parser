from dataclasses import dataclass

from app.domain.entities.base import BaseEntity
from app.domain.values.brand import NameOfBrand


@dataclass(eq=False)
class Brand(BaseEntity):
    name: NameOfBrand

    __hash__ = BaseEntity.__hash__
    __eq__ = BaseEntity.__eq__
