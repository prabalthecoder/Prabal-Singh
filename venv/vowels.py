str = input("enter the string : ")
list = [ c for c in str if c in ('a', 'e', 'i', 'o', 'u')]
print(len(list))