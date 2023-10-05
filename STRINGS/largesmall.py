s=input("enter a string: ")
large=s[0]
small=s[0]
for ch in s:
    if(ch>large):
        large=ch
    elif(ch<small):
        small=ch
print('Large:',large, 'small:',small)
