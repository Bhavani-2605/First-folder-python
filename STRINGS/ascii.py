#program to print ASCII values of a string
s=input("Enter a string: ")
for char in s:
    print("ASCII value of "+char+":",ord(char))