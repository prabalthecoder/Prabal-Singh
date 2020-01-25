'''with open("try.txt","w") as file:
    file.write("hello world qwerty qwerty")


with open("try.txt","r") as file:
    print(file.read())'''


try:
    num = input("enter the number")
    print(num /0)

except Exception as exp:
    print("error is jhgjgjhgjhg {0}".format(exp))

