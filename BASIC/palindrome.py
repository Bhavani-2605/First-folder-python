num=int(input())
dup=num
rev=0
while(num!=0):
    r=num%10
    rev=rev*10+r
    num=num//10
if(rev==dup):
    print(dup,'is palindrome')
else:
    print(dup,'is not a palindrome')