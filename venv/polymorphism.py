class Base:

    def display(self):
        print("I am from base")


class Derived(Base): #Inheriting Base in Derived class

    def display(self):
        print("I am for derived")
        super().display()


def main():
    objderived = Derived()
    objderived.display()


if __name__ == "__main__":
    main()
