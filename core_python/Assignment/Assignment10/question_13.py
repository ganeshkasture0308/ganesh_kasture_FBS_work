n = int(input("Enter the number of elements: "))
numbers = []

for i in range(n):
    num = int(input(f"Enter element {i+1}: "))
    numbers.append(num)

updated_list = []
for num in numbers:
    if num % 2 != 0:
        updated_list.append(num)

print("List after removing even numbers:", updated_list)
