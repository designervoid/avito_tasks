def last(o):
    it = o.__iter__()
    e = next(it)
    while True:
        try:
            nxt = next(it)
            yield (False, e)
            e = nxt
        except StopIteration:
            yield (True, e)
            break


for i in last(range(4)):
    print(i)
