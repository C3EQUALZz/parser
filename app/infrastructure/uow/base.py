from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from typing import Self, List, Generator

from app.logic.events.base import AbstractEvent


@dataclass(frozen=True)
class AbstractUnitOfWork(ABC):
    """
    Interface for any units of work, which would be used for transaction atomicity, according DDD.
    """
    _events: List[AbstractEvent] = field(default_factory=list)

    async def __aenter__(self) -> Self:
        return self

    async def __aexit__(self, *args, **kwargs) -> None:
        await self.rollback()

    @abstractmethod
    async def commit(self) -> None:
        raise NotImplementedError

    @abstractmethod
    async def rollback(self) -> None:
        raise NotImplementedError

    async def add_event(self, event: AbstractEvent) -> None:
        self._events.append(event)

    def get_events(self) -> Generator[AbstractEvent, None, None]:
        """
        Using generator to get elements only when they needed.
        Also, can not use self._events directly, not to run events endlessly.
        """

        while self._events:
            yield self._events.pop(0)
