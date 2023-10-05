#Program to swap two elements in a list

l2=[10,20,30,40,50]
pos1=int(input('enter pos1: '))
pos2=int(input('enter pos2: '))
print(l2)
l2.insert(pos2-1,l2.pop(pos1-1))
l2.insert(pos1-1,l2.pop(pos1))
print(l2)