from typing import List, Any, TypeVar, Callable, Iterable

T = TypeVar("T")


def append(list1: List[T], list2: List[T]) -> List[T]:
    return list1 + list2


def concat(lists: List[List[T]]) -> List[T]:
    return [x for l in lists for x in l]


def filter(function: Callable, list: List[T]) -> List[T]:
    return [x for x in list if function(x)]


def length(list: Iterable) -> int:
    return sum(1 for _ in list)


def map(function: Callable, list: List[T]) -> List[Any]:
    return [function(x) for x in list]


def foldl(function: Callable, list: List[T], initial: T) -> T:
    acc = initial
    for item in list:
        acc = function(acc, item)
    return acc


def foldr(function: Callable, list: List[T], initial: T) -> T:
    acc = initial
    for item in reverse(list):
        acc = function(item, acc)
    return acc


def reverse(list: List[T]) -> List[T]:
    return list[::-1]
