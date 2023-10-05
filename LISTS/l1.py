#Program to interchange first and last elements in a list

n=int(input('enter n: '))
l1=[]
for i in range(n):
    ele=int(input())
    l1.append(ele)
print(l1)

l1.insert(0,l1.pop())
l1.append(l1.pop(1))
print(l1)