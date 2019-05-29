def first(iterable, condition=lambda x: True):
    if iterable != 0:
        return next(x for x in iterable if condition(x))
    elif iterable == 0:
        return None


foo = (x for x in range(10))
print(first(foo))
print(first(0))
