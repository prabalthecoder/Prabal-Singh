def myGenFunc():
    v = 2
    yield v

    v = 3
    yield v

    v = 4
    yield v

gen_obj= myGenFunc()
print(next(gen_obj))
print(next(gen_obj))
print(next(gen_obj))

