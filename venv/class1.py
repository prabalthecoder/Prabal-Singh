class Parrot:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def sing(self, song ):
        print("{0} sings {1} song".format(self.name, song))

    def dance(self):
        print("{0} is now dancing".format(self.name))

def main():
    HelloObj = Parrot("Hello", 4)
    LehhoObj = Parrot("Lehho", 5)

    HelloObj.sing('yoyo')
    LehhoObj.sing('oyoy')

    HelloObj.dance()
    LehhoObj.dance()


if __name__ == "__main__":
    main()