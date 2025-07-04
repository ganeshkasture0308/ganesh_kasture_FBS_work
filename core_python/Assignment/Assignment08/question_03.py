# 3. Write a program to find sum of following series using functions : 
# a.  1+ 2 + 3 + 4+….. + n 
# b. 1!+ 2! + 3! + 4!+….. + n! 
# c. 1^1 + 2^2 + 3^3+ …… n^n 

#a.1+ 2 + 3 + 4+….. + n 
def sum_natural(n):
    total = 0
    for i in range(1, n + 1):
        total += i
    return total
num = int(input("Enter value of n: "))
result = sum_natural(num)
print("Sum:", result)
print("###############################################")

#b.1!+ 2! + 3! + 4!+….. + n! 
def factorial(num):
    fact = 1
    for i in range(1, num + 1):
        fact *= i
    return fact

def sum_of_factorials(n):
    total = 0
    for i in range(1, n + 1):
        total += factorial(i)
    return total
num = int(input("Enter the value of n: "))
result = sum_of_factorials(num)
print("Sum of factorials:", result)
print("#######################################################")


#c. 1^1 + 2^2 + 3^3+ …… n^n 
def sum_of_powers(n):
    total = 0
    for i in range(1, n + 1):
        total += i ** i
    return total

# Input from user
num = int(input("Enter the value of n: "))
result = sum_of_powers(num)
print("Sum of the series:", result)

