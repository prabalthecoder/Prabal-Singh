class Abc:
    #instance method because of self
    def sum(self,num1, num2):
        num3 = num1 + num2
        return num3

    @staticmethod
    def display(number):
        print("the sum is {0}".format(number))

def main():
    prabalobj = Abc() #instantiation of a class
    result = prabalobj.sum(10, 1) #calling sum method and reciving result

    Abc.display(result)

if __name__ == "__main__":
    main()


