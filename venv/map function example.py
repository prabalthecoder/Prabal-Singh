
a = [-2, -1, 0, 1, 2, 3, 4, 5, 6, 7]
def sqr(num):
    return  num ** 2
b = list(map(sqr, a))
print(b)

c = [-2, -1, 0, 1, 2, 3, 4, 5, 6, 7]
d = list(map(lambda x : x ** 2, c))
print(d)

c = [-2, -1, 0, 1, 2, 3, 4, 5, 6, 7]
d = list(filter(lambda x : x % 2, c))
print(d)