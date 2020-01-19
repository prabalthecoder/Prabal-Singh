from functools import reduce

a = [2, 3, 4, 5, 6, 7, 10]
def red(num1, num2):
    return num1 + num2
b = reduce(red, a)
print(b)

c = [2, 3, 4, 5, 6, 7, 10, 11]
d = reduce(lambda num1 ,num2 : num1 + num2 ,c)
print(d)