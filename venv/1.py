def sum(num1, num2):
    num3 = num1 + num2
    print("Sum of {0}, {1} is : {2}".format(num1, num2, num3))


def sub(num1, num2):
    num3 = num1 - num2
    print("Sub of {0}, {1} is : {2}".format(num1, num2, num3))


def mul(num1, num2):
    num3 = num1 ** num2
    print("Mul of {0}, {1} is : {2}".format(num1, num2, num3))


def div(num1, num2):
    num3 = num1 // num2
    print("div of {0}, {1} is : {2}".format(num1, num2, num3))


def mod(num1, num2):
    num3 = num1 % num2
    print("mod of {0}, {1} is : {2}".format(num1, num2, num3))


def floor(num1, num2):
    num3 = num1 // num2
    print("floor of {0}, {1} is : {2}".format(num1, num2, num3))


def power(num1, num2):
    num3 = num1 ** num2
    print("power of {0}, {1} is : {2}".format(num1, num2, num3))


def lessthan(num1, num2):
    num3 = num1 < num2
    print("< of {0}, {1} is : {2}".format(num1, num2, num3))


def greater(num1, num2):
    num3 = num1 > num2
    print("> of {0}, {1} is : {2}".format(num1, num2, num3))


def comparision(num1, num2):
    num3 = num1 == num2
    print("comparision of {0}, {1} is : {2}".format(num1, num2, num3))


def notequal(num1, num2):
    num3 = num1 != num2
    print("notequal of {0}, {1} is : {2}".format(num1, num2, num3))


def Greaterthanorequalto(num1, num2):
    num3 = num1 >= num2
    print("Greaterthanorequalto of {0}, {1} is : {2}".format(num1, num2, num3))


def lessthanorequalto(num1, num2):
    num3 = num1 <= num2
    print("lessthanorequalto of {0}, {1} is : {2}".format(num1, num2, num3))


def bitwiseor(num1, num2):
    num3 = num1 | num2
    print("bitwiseor of {0}, {1} is : {2}".format(num1, num2, num3))


def bitwiseand(num1, num2):
    num3 = num1 & num2
    print("bitwiseand of {0}, {1} is : {2}".format(num1, num2, num3))


def bitwisenot(num1 ):
    print(~num1)


def bitwiserightshift(num1):
    print(num1 >> 2)


def bitwiseleftshift(num1):
    print(num1 << 2)


# wrong answer
def bitwisexor(num1, num2):
    num3 = num1 ^ num2
    print("bitwisexor of {0}, {1} is : {2}".format(num1, num2, num3))


def addand(num1, num2):
    num1 += num2
    print(num1)

def suband(num1, num2):
    num1 -= num2
    print(num1)


def muland(num1, num2):
    num1 *= num2
    print (num1)

def divand(num1, num2):
    num1 /= num2
    print(num1)

def modand(num1, num2):
    num1 %= num2
    print(num1)

def floorand(num1, num2):
    num1 //= num2
    print(num1)


def powerand(num1, num2):
    num1 **= num2
    print(num1)

def bitwiseandequal(num1, num2):
    num1 &= num2
    print(num1)

#wrong
def bitwisenotequal(num1):
    print("answer is:{0}".format(~num1))


def bitwiseorequal(num1, num2):
    num1 |= num2
    print(num1)


def bitwiserightequal(num1):
    num1 <<= 2
    print(num1)

def bitwiseleftequal(num1):
    num1 >>= 2
    print(num1)

def bitwisexorequal(num1, num2):
    num1 ^= num2
    print(num1)

def specialis(num1, num2):
    print(num1 is num2)

def specialisnot(num1, num2):
    print(num1 is not num2)

def memberin(num1):
    print("banana" in num1)

def membernotin(num1):
    print("hello" not in num1)

def main():
    sum(2, 3)
    sub(2, 3)
    mul(2, 3)
    div(2, 3)
    mod(2, 3)
    floor(2, 3)
    power(2, 3)
    lessthan(4, 3)
    greater(2, 3)
    comparision(2, 3)
    notequal(2, 3)
    Greaterthanorequalto(2, 3)
    lessthanorequalto(2, 3)
    bitwiseor(2, 3)
    bitwiseand(2, 3)
    bitwisenot(2)
    bitwiserightshift(10)
    bitwiseleftshift(10)
    bitwisexor(2, 3)
    addand(10, 5)
    suband(10, 5)
    muland(10, 5)
    divand(10, 5)
    modand(10, 5)
    floorand(10, 5)
    powerand(10, 5)
    bitwiseandequal(2, 3)
    bitwisenotequal(2)
    bitwiseorequal(2, 3)
    bitwiserightequal(10)
    bitwiseleftequal(10)
    bitwisexorequal(2, 3)
    specialis("apple", "apple")
    specialisnot("apple", "apple")
    memberin("apple" "banana")
    membernotin("apple" "banana")


if __name__ == "__main__":
    main()

