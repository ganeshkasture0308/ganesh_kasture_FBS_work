
n = int(input("Enter number of elements: "))


numbers = []


for i in range(n):
    num = int(input(f"Enter element {i+1}: "))
    numbers.append(num)


even_list = []
odd_list = []


for num in numbers:
    if num % 2 == 0:
        even_list.append(num)
    else:
        odd_list.append(num)

print("Original List:", numbers)
print("Even Elements:", even_list)
print("Odd Elements:", odd_list)
