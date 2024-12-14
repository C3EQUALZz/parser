from abc import ABC
from dataclasses import dataclass

from app.domain.entities.base import BaseEntity


@dataclass(eq=False)
class BaseAggregateRoot(BaseEntity, ABC):
    ...
