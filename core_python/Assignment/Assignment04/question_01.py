#1. WAP to print all even numbers until n.

n=int(input("enter the value of n:"))
print("Even number from 1 to ",n,"are:")
for i in range (2,n+1,2):
    print(i)