#sum of series
#sum of first n numbers
n=int(input("enter the number:"))
fact=0
for i in range(0,n+1):
    fact=fact+i

print(f'factorial of {n} is:{fact}')