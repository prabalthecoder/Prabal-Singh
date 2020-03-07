class Base:
    def __init__(self):
        self.a = 5


class Derived1(Base):
    def __init__(self):
        super().__init__()
        self.b = 7


class Derived2(Derived1):
    def __init__(self):
        super().__init__()
        self.c = 10

    def sum(self):
        result = self.a + self.b + self.c
        return result

    @staticmethod
    def display(number):
        print("the sum is {0}".format(number))


def main():
    prabalobj = Derived2()
    result = prabalobj.sum()
    Derived2.display(result)


if __name__ == "__main__":
    main()