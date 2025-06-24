#3. WAP to print sum of series upto n. 

n=int(input("enter the value of n:"))

total=0
for i in range(1,n+1):
    total+=i
print("sum of series from 1 to",n,"are:",total)
