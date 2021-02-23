import collections

from typing import Any
from typing import Iterable


def flatten(iterable: Iterable[Any]) -> Iterable[Any]:
    result = []
    for item in iterable:
        if isinstance(item, collections.Iterable):
            result.extend(flatten(item))
        elif item is not None:
            result.append(item)
    return result
