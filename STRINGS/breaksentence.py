#program to break sentence into words
s=input("enter a string: ")
word=1
for ch in s:
    if(ch!=' '):
        print(ch,end='')
    else:
        print('\nword:',word)
        word=word+1
print('\nword:',word)
