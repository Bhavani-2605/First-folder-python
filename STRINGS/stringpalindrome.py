#program to check a string is palindrome or not
s=input("enter a string: ")
rev=''
for i in range(len(s)-1,-1,-1):
    rev=rev+s[i] 
print('Reverse string:',rev)
if(s==rev):
    print('palindrome')
else:
    print('not a palindrome')