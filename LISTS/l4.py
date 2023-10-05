#Program to check if element exists in a list

l4=[10,20,34,56,74,2,13,68,36,99]
flag=0
ele=int(input('enter elememt: '))
for i in l4:
    if(i==ele):
        flag=1
        break
if(flag==1):
    print('Found')
else:
    print('not found')