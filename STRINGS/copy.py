#program to copy specific portion of a string
s=input('enter a string')
si=int(input('enter starting index: '))
ei=int(input('enter ending index: '))
cpystr=s[si:ei+1]
print(cpystr)