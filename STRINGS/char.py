#program to check whether a character is upper or lower
char=input("enter a character: ")
if(char>='a' and char<='z'):
    print('lower')
elif(char>='A' and char<='Z'):
    print('upper')
else:
    print('you entered a special character!!!')