#5. WAP to print Fibonacci series upto n.
n = int(input("Enter the value of n: "))
a, b = 0, 1
print("Fibonacci series up to", n, "is:")
while a <= n:
    print(a, end=" ")
    a, b = b, a + b 