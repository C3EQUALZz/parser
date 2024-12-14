from dataclasses import dataclass
from typing import List

from typing_extensions import override

from app.domain.values.base import BaseValueObject


@dataclass(frozen=True)
class Link(BaseValueObject[str]):
    value: str

    @override
    def validate(self) -> None:
        ...

    @override
    def as_generic_type(self) -> str:
        return self.value


@dataclass(frozen=True)
class Article(BaseValueObject[int]):
    value: int

    @override
    def validate(self) -> None:
        ...

    @override
    def as_generic_type(self) -> int:
        return self.value


@dataclass(frozen=True)
class Name(BaseValueObject[str]):
    value: str

    @override
    def validate(self) -> None:
        ...

    @override
    def as_generic_type(self) -> str:
        return self.value


@dataclass(frozen=True)
class Brand(BaseValueObject[str]):
    value: str

    @override
    def validate(self) -> None:
        ...

    @override
    def as_generic_type(self) -> str:
        return self.value


@dataclass(frozen=True)
class BrandId(BaseValueObject[int]):
    value: int

    @override
    def validate(self) -> None:
        ...

    @override
    def as_generic_type(self) -> int:
        return self.value


@dataclass(frozen=True)
class Price(BaseValueObject[int]):
    value: int

    @override
    def validate(self) -> None:
        ...

    @override
    def as_generic_type(self) -> int:
        return self.value


@dataclass(frozen=True)
class Rating(BaseValueObject[int]):
    value: int

    @override
    def validate(self) -> None:
        ...

    @override
    def as_generic_type(self) -> int:
        return self.value


@dataclass(frozen=True)
class FeedBacks(BaseValueObject[List[str]]):
    value: List[str]

    @override
    def validate(self) -> None:
        ...

    @override
    def as_generic_type(self) -> List[str]:
        return self.value
