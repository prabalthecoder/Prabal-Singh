class Abc:

    def __init__(self, radius):
        self.radius = radius
        b = 22/7
        self.pi = b

    def area(self):
        num3 = (self.radius ** 2) * self.pi
        return num3

    def perimeter(self):
        num4 = self.radius * 2 * self.pi
        return num4

    @staticmethod
    def display(number):
        print("the area of circle is {0}".format(number))

    @staticmethod
    def display1(number):
        print("the area of circle is {0}".format(number))


def main():
    r = int(input("enter radius:"))
    circleobj = Abc(r)
    result = circleobj.area()
    Abc.display(result)
    result = circleobj.perimeter()
    Abc.display1(result)


if __name__ == "__main__":
    main()