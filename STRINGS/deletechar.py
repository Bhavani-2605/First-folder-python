#program to delete a character in a string
s=input("enter a string: ")
char=input('enter a character: ')
for ch in s:
    if(ch==char):
        continue
    print(ch,end='')