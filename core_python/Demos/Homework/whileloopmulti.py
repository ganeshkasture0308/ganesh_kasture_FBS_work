#multiplication of two number using while looop.
num1 = int(input("Enter first positive number: "))
num2 = int(input("Enter second positive number: "))
result = 0
count = 0
while count < num2:
    result += num1
    count += 1
print("Multiplication result:", result)
