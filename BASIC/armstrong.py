n=int(input())
dup=n
arm=0
while(n!=0):
    r=n%10
    arm=r**3+arm
    n=n//10
if(arm==dup):
    print(dup,'is an armstrong number')
else:
    print(dup,'is not an armstrong number')