from dataclasses import dataclass
from typing import override

from app.domain.values.base import BaseValueObject


@dataclass(frozen=True)
class NameOfMarketplace(BaseValueObject[str]):
    value: str

    @override
    def validate(self) -> None:
        ...

    @override
    def as_generic_type(self) -> str:
        return self.value


@dataclass(frozen=True)
class MarketPlaceUrl(BaseValueObject[str]):
    value: str

    @override
    def validate(self) -> None:
        ...

    @override
    def as_generic_type(self) -> str:
        return self.value
