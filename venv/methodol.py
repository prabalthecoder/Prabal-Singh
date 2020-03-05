def sum(num1, num2):
    num3 = num1 + num2
    print("Sum of {0}, {1} is : {2}".format(num1, num2, num3))


def sum(num1, num2, num3):
    num4 = num1 + num2 + num3
    print("Sum of {0}, {1}, {2} is : {3}".format(num1, num2, num3, num4))


def main():
    sum(3, 2, 3)


if __name__ == "__main__":
    main()
