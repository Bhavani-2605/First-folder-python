n=int(input('enter n: '))
l=[]
count=0
for i in range(n):
    ele=int(input())
    l.append(ele)
ele=int(input('enter element: '))
for i in l:
    if(i==ele):
        count=count+1
print('count: ',count)