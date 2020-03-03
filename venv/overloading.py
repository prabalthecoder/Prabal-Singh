class Point:

    def __init__(self, x=0, y=0):
        self.a = x
        self.b = y

    def __add__(self, otherObj):
        obj = Point()

        obj.a = self.a * otherObj.a
        obj.b = self.b * otherObj.b

        return obj

def main():
    object1 = Point(12, 13)
    object2 = Point(4, 5)

    object3 = object1 + object2

    print(object3.a)
    print(object3.b)


if __name__ == "__main__":
    main()

