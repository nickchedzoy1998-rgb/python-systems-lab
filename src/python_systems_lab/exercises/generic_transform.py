from collections.abc import Callable, Iterable
from typing import TypeVar

T = TypeVar("T")
U = TypeVar("U")

def transform_items(
    items: Iterable[T],
    transform: Callable[[T], U],
) -> list[U]:
    return [transform(itm) for itm in items]