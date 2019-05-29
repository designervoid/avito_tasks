from collections import deque

last_getter = deque(maxlen=1)
seq = range(0)
iseq = iter(seq)

first = last = next(iseq, None)
last_getter.extend(iseq)
if last_getter:
    last = last_getter[0]

print(first, last)
