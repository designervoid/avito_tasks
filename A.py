a, b, c = int(input()), int(input()), int(input())
if a < b and a < c:
    if b < c:
        print(a, b, c)
    else:
        b, c = c, b
        print(a, b, c)
if b < a and b < c:
    if a < c:
        a, b = b, a
        print(a, b, c)
    else:
        a, b = b, a
        b, c = c, b
        print(a, b, c)
if c < a and c < b:
    if a < b:
        a, b = c, b
        b, c = a, b
        print(a, b, c)
    else:
        a, b = b, a
        b, c = c, b
        a, b = b, a
        print(a, b, c)
