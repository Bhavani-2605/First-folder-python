nterms = int(input("nth: "))
n1, n2 = 0, 1
count = 0
if nterms <= 0:
   print("Please enter a positive integer")
# if there is only one term, return n1
elif nterms == 1:
   print("Fibonacci sequence upto",nterms,":",end=" ")
   print(n1)
# generate fibonacci sequence
else:
   print("Fibonacci sequence: ",end="")
   while count < nterms:
       print(n1,end=" ")
       nth = n1 + n2
       # update values
       n1 = n2
       n2 = nth
       count += 1

