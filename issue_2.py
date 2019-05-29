import collections
from collections.abc import Iterable


def flatten(iterable: Iterable):
    for elem in iterable:
        if isinstance(elem, collections.Iterable):
            yield from flatten(elem)
        else:
            yield elem


print(list(flatten([0, [1, [2, 3]]])))
