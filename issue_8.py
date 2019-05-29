import itertools

my_list = (i for i in range(10))
top5 = itertools.islice(my_list, 0, 5)
print(list(top5))


def reversed_iterator(iter):
    return reversed(list(iter))


print(list(reversed_iterator(my_list)))

print(list(reversed(list(i for i in range(10)))))
