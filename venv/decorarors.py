def func1(msg):
    def nested_function():
        print("black")
        msg()
    return nested_function


@func1
def func2():
    print("this is the main method")


def main():
    func2()


if __name__ == "__main__":
    main()
