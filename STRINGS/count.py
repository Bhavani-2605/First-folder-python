#program to calculate number of characters,vowels,consonants,words and white spaces in a string
s=input('enter a string: ')
characters=0
vowels=0
consonants=0
words=0
space=0
for ch in s:
    characters=characters+1
    if(ch in 'aeiouAEIOU'):
        vowels=vowels+1
    elif(ch==' '):
        space=space+1
    else:
        consonants=consonants+1
print('words:',space+1,'characters:',characters,'vowels:',vowels,'spaces:',space,'consonants:',consonants)