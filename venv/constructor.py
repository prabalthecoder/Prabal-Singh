class Abc:

    def __init__(self, a, b):
        self.num1 = a
        self.num2 = b

    def sum(self):
        num3 = self.num1 + self.num2
        return num3

    @staticmethod
    def display(number):
        print("the sum is {0}".format(number))


def main():
    prabalobj = Abc(2, 13)
    result = prabalobj.sum()

    Abc.display(result)


if __name__ == "__main__":
    main()