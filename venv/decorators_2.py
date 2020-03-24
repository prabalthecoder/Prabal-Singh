def smart_divide(msg):
    def nested_func(a, b):
        if b == 0:
            print("sorry")
            return
        msg(a, b)
    return nested_func

@smart_divide
def divide(a, b):
    c = a / b
    return c

def main():
    divide(10, 5)

if __name__ == "__main__":
    main()




