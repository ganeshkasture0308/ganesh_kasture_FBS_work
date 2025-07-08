n = int(input("Enter how many numbers: "))
numbers = []
squares = []
cubes = []

for i in range(n):
    num = int(input(f"Enter number {i+1}: "))
    numbers.append(num)
    squares.append(num ** 2)
    cubes.append(num ** 3)

print("Numbers:", numbers)
print("Squares:", squares)
print("Cubes:", cubes)
