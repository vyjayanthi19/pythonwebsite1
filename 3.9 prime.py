n=5 
factors=0
for i in range(2,n):
    if (n%i ==0 ):
       factors= factors+1 
    if factors==0:
        print("Prime number")
    else:
        print("Not a Prime number")
