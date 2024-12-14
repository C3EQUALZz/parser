from dataclasses import dataclass

from app.domain.entities.base import BaseEntity
from app.domain.values.marketplace import NameOfMarketplace, MarketPlaceUrl


@dataclass(eq=False)
class Marketplace(BaseEntity):
    name: NameOfMarketplace
    url: MarketPlaceUrl

    __hash__ = BaseEntity.__hash__
    __eq__ = BaseEntity.__eq__
