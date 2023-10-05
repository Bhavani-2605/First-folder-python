#Program to Count no of occurrences of a given element in a list

count=0
l7=[1,2,4,6,3,2,9,6,7,2,4,5,6,6,7]
print(l7)
ele=int(input('enter element: '))
for i in l7:
    if(i==ele):
        count=count+1
print('count: ',count)