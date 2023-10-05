#program to delete all the spaces in a sentence
s=input("enter a string: ")
for ch in s:
    if(ch==' '):
        continue
    else:
        print(ch,end='')