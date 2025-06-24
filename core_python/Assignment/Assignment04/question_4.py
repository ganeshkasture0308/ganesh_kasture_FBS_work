#4. WAP to print factorial of a number . 

n=int(input("enter the number:"))
factorial=1
for i in range(1,n+1):
    factorial*=i

print("factorial of",n,"is:",factorial)