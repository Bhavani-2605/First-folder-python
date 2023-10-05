'''
n=int(input())
sum=0
for i in range(1,n+1):
    sum=sum+i
print("Sum of 1 to",n,"numbers:",sum)

n=int(input())
pro=1
for i in range(1,n+1):
    pro=pro*i
print("Product of 1 to",n,"numbers:",pro)
'''
num = int(input())

# let's take a syntax for our table - num x (1 - 10) = num*(1-10)
# Since we're taking the table to 10, hence we'll iterate it 10 times
n=int(input())
print("The multiplication table of", num)
for i in range(1, n+1):
    print(f" {num} x {i} = {num*i}")