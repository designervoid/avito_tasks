import itertools


def grouper(n, iterable):
    it = iter(iterable)
    while True:
        chunk = tuple(itertools.islice(it, n))
        if not chunk:
            return
        yield chunk


print(list(grouper(3, [0, 1, 2, 3, 4])))
