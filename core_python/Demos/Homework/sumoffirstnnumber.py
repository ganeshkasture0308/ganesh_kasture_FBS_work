#sum of series
#sum of first n numbers
n=int(input("enter the number:"))
sum=0
for i in range(0,n+1):
    sum=sum+i

print(f'sum of first n number: {n} is:{sum}')