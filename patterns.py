'''
*****
*****
*****
*****
*****
n=5
for row in range(1,n+1):
    for col in range(1,n+1):
        print('*',end=' ')
    print()

*
**
***
****
*****
n=5
for row in range(1,n+1):
    for col in range(1,row+1):
        print('*', end=' ')
    print()

1
12
123
1234
12345
n=5
for row in range(1,n+1):
    for col in range(1,row+1):
        print(col, end=' ')
    print()

1
22
333
4444
55555
n=5
for row in range(1,n+1):
    for col in range(1,row+1):
        print(row, end=' ')
    print()

*****
****
***
**
*
n=5
for row in range(1,n+1):
    for col in range((n+1)-row,0,-1):
        print('*', end=' ')
    print()

11111
2222
333
44
5
n=5
for row in range(1,n+1):
    for col in range((n+1)-row,0,-1):
        print(row, end=' ')
    print()
    
12345
1234
123
12
1
n=5
for row in range(1,n+1):
    for col in range(1,(n+2)-row):
        print(col, end=' ')
    print()

    1
   12
  123
 1234
12345
n=5
for row in range(1,n+1):
    for space in range(n-row,0,-1):
        print(' ', end=' ')
    for col in range(1,row+1):
        print(col,end=' ')
    print()
    
*********
 *******
  *****
   ***
    *
n=5
d=0
for row in range(1,n+1):
    for space in range(1,row+1):
        print(' ', end=' ')
    for col in range(1,(n*2)+d):
        print('*',end=' ')
    d=d-2
    print()

'''

    