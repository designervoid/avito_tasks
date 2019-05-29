from collections import OrderedDict


def distinct(obj):
    return OrderedDict.fromkeys(obj)


t = [1, 2, 3, 1, 2, 5, 6, 7, 8]
print(list(distinct(t)))
