from dataclasses import dataclass

from app.logic.commands.base import AbstractCommand


@dataclass(frozen=True)
class ParseAllProductsFromACertainNumberOfPagesWithKeyName(AbstractCommand):
    key_word: str
    count_of_pages: int


@dataclass(frozen=True)
class ParseCategory(AbstractCommand):
    name: str


@dataclass(frozen=True)
class GetAllCategories(AbstractCommand):
    ...
