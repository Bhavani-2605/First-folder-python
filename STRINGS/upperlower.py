#program to count the upper and lower case characters in a string
s=input("enter a string: ")
uppercnt=0
lowercnt=0
for ch in s:
    if(ch>='a' and ch<='z'):
        lowercnt=lowercnt+1
    elif(ch>='A' and ch<='Z'):
        uppercnt=uppercnt+1
print('upper count= ',uppercnt)
print('lower count= ',lowercnt)