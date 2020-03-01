class MyClass:
    #Constructor
    def __init__(self, num1, num2):
        self.number1 = num1 #Assigning num1 value to self.number1
        self.number2 = num2


    def display1(self):
        print("sum of {0} and {1} is: {2}".format(self.number1, self.number2, self.number3))


    def display(self):
        print("mul of {0} and {1} is: {2}".format(self.number1, self.number2, self.number3))

    def display2(self):
        print("sub of {0} and {1} is: {2}".format(self.number1, self.number2, self.number3))


    def display3(self):
        print("div of {0} and {1} is: {2}".format(self.number1, self.number2, self.number3))

    def mul(self):
        self.number3 = self.number1 * self.number2

    def sum(self):
        self.number3 = self.number1 + self.number2

    def div(self):
        self.number3 = self.number1 / self.number2

    def sub(self):
        self.number3 = self.number1 - self.number2

def main(): #Driver function

    number1 = int(input("Enter number 1:"))
    number2 = int(input("Enter number 2:"))

    #instantiate the class
    prabalsObj = MyClass(number1,number2)

    prabalsObj.sum()
    prabalsObj.display1()
    prabalsObj.mul()
    prabalsObj.display()
    prabalsObj.sub()
    prabalsObj.display2()
    prabalsObj.div()
    prabalsObj.display3()

if __name__ == "__main__":
    main()