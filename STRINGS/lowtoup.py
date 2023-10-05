#program to convert the string from lower to upper
s=input("enter a string: ")
ustr=' '
for ch in s:
    if(ch>='A' and ch<='Z'):
        pass
    elif(ch>='a' and ch<='z'):
        ustr=ustr+chr(ord(ch)-32)
print('LOWER to UPPER:',ustr)