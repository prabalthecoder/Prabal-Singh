class Base:

    def display(self):
        print("I am from base")


class Derived:

    def display(self):
        print("I am for derived")
        Base().display()


def main():
    objderived = Derived()
    objderived.display()


if __name__ == "__main__":
    main()