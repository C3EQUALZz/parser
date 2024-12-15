from abc import ABC

from app.infrastructure.services.parsers.base import MarketPlaceParser


class AbstractWildBerriesParser(MarketPlaceParser, ABC):
    ...
