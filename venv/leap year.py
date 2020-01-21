def module(num1, num2):
    if (num1 % 4) == 0:
     if (num1 % 100) == 0:
        if (num1 % 400) == 0:
                print("{0} is a leap year".format(num1))
        else:
                print("{0} is not a leap year".format(num1))
     else:
            print("{0} is a leap year".format(num1))
    else:
        print("{0} is not a leap year".format(num1))


def main():
    module(2100, 4)

if __name__ == "__main__":
    main()