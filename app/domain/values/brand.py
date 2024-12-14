from dataclasses import dataclass
from typing import override

from app.domain.values.base import BaseValueObject


@dataclass(frozen=True)
class NameOfBrand(BaseValueObject[str]):
    value: str

    @override
    def validate(self) -> None:
        ...

    @override
    def as_generic_type(self) -> str:
        return self.value