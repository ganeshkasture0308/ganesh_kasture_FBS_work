count = int(input("Enter the number of elements in the list: "))
numbers = []
for i in range(count):
    num = int(input(f"Enter element {i+1}: "))
    numbers.append(num)

m = int(input("Enter the value of m: "))
n = int(input("Enter the value of n: "))

print(f"Numbers divisible by both {m} and {n} are:")
for num in numbers:
    if num % m == 0 and num % n == 0:
        print(num)
