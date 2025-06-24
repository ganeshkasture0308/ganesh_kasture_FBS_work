def sos(n):
    if(n==0):
        return 0
    else:
        return n+sos(n-1)
n=int(input("enter the number for sum of series:"))
print("Addition:",sos(n))