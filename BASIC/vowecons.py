ch=input('Enter a character: ')
if(ch in 'aeiouAEIOU'):
    print('Vowel')
elif(ch>'a' and ch<='z' or ch>='A' and ch<='Z'):
    print('Consonant')
else:
    print('Enter alphabets only!!!')