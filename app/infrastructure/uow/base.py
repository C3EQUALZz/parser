from abc import ABC, abstractmethod
from dataclasses import field
from typing import List, Generator
from typing import Self

from sqlalchemy.ext.asyncio import async_sessionmaker, AsyncSession

from app.logic.events.base import AbstractEvent


class AbstractUnitOfWork(ABC):
    """
    Interface for any units of work, which would be used for transaction atomicity, according DDD.
    """

    def __init__(self) -> None:
        self._events: List[AbstractEvent] = field(default_factory=list)

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


class SQLAlchemyAbstractUnitOfWork(AbstractUnitOfWork):
    """
    Unit of work interface for SQLAlchemy, from which should be inherited all other units of work,
    which would be based on SQLAlchemy logics.
    """

    def __init__(self, session_factory: async_sessionmaker = default_session_factory) -> None:
        super().__init__()
        self._session_factory: async_sessionmaker = session_factory

    async def __aenter__(self) -> Self:
        self._session: AsyncSession = self._session_factory()
        return await super().__aenter__()

    async def __aexit__(self, *args, **kwargs) -> None:
        await super().__aexit__(*args, **kwargs)
        await self._session.close()

    async def commit(self) -> None:
        await self._session.commit()

    async def rollback(self) -> None:
        """
        Rollbacks all uncommited changes.

        Uses self._session.expunge_all() to avoid sqlalchemy.orm.exc.DetachedInstanceError after session rollback,
        due to the fact that selected object is cached by Session. And self._session.rollback() deletes all Session
        cache, which causes error on Domain model, which is not bound now to the session and can not retrieve
        attributes.

        https://pythonhint.com/post/1123713161982291/how-does-a-sqlalchemy-object-get-detached
        """

        self._session.expunge_all()
        await self._session.rollback()
