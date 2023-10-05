l1=['red','blue','green','yellow','black']
l2=[1,2,3,4,5]
print(l1) #['red', 'blue', 'green', 'yellow', 'black']
print(l1[0]) #red
print(l1[-1])   #black
print(l1+l2)    #['red', 'blue', 'green', 'yellow', 'black', 1, 2, 3, 4, 5]
print(l1*2,l2*2)    #['red', 'blue', 'green', 'yellow', 'black', 'red', 'blue', 'green', 'yellow', 'black'] [1, 2, 3, 4, 5, 1, 2, 3, 4, 5]
print('black' in l1)    #True
print('red' not in l1)  #False
print(l1[0:6])  #['red', 'blue', 'green', 'yellow', 'black']
print(l1[0:6:2])    #['red', 'green', 'black']
print(l1[0:6:-1])   #[]
print(l1[::2])  #['red', 'green', 'black']
print(l1[::-1]) #['black', 'yellow', 'green', 'blue', 'red']
print(l1[6])    #IndexError: list index out of range
