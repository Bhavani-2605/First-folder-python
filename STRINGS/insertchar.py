#program to insert the character into the string at the given location
s=input('enter a string: ')
loc=int(input('enter location: '))
insert=input('enter character to be inserted: ')
print(s[:loc]+insert+s[loc:])