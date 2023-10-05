#program to convert the string from upper to lower
s=input("enter a string: ")
lstr=' '
for ch in s:
    if(ch>='a' and ch<='z'):
        lstr='you entered in lowercase'
    elif(ch>='A' and ch<='Z'):
        lstr=lstr+chr(ord(ch)+32)
print('UPPER to LOWER:',lstr)