from collections.abc import Iterable


def ilen(iterable: Iterable):
    test = sum(1 for i in iterable)
    return test


foo = (x for x in range(20))
print(ilen(foo))
