#program to delete all the vowels in a sentence
s=input("enter a string: ")
for ch in s:
    if(ch in 'aeiouAEIOU'):
        continue
    else:
        print(ch,end='')