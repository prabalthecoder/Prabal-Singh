from functools import reduce

a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

c = list(filter(lambda x : x % 2 == 0, a))
print(c)
d = list(map(lambda x : x ** 2, c))
print(d)
e = reduce(lambda num1 ,num2 : num1 + num2 ,d)
print(e)
