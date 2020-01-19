a = [-2, -1, 0, 1, 2, 3, 4, 5, 6, 7]
def even(num):
    if num % 2 == 0:
        return 1
b = list(filter(even, a))
print(b)

a = [-2, -1, 0, 1, 2, 3, 4, 5, 6, 7]
c = list(filter(lambda x : x % 2 == 0, a))
print(c)

