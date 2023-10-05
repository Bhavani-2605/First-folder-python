#program to count the frequency of a character in a string
s=input("enter a string: ")
ch=input("enter a character: ")
count=0
for char in s:
    if(char==ch):
        count=count+1
print(count)