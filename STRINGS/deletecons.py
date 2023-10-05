#program to delete all the consonants in a sentence
s=input("enter a string: ")
for ch in s:
    if(ch not in 'aeiouAEIOU'):
        continue
    else:
        print(ch,end='')