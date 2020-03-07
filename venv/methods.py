from datetime import date


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def fromYear(cls, name, year):
        return cls(name, date.today().year - year)


    @staticmethod
    def checkAdult(age):
        if age > 18:
            print("Adult")

        else:
            print("Minor")

def main():
    obj1 = Person('prabal', 15)
    obj2 = Person.fromYear('Tom', 2000)

    # print(obj1)
    # print(obj2)

    Person.checkAdult(obj1.age)
    Person.checkAdult(obj2.age)


if __name__ == "__main__":
    main()