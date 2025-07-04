def fact(n):
    if n == 1 or n == 0:
        return 1
    else:
        return n * fact(n - 1)
def sum_of_series(n):
    if n == 1:
        return fact(1)  
    else:
        return fact(n) + sum_of_series(n - 1)
num = int(input("Enter value of n: "))
result = sum_of_series(num)
print("Sum of the series 1! + 2! + ... +", num, "! is:", result)
