# 1. Python Program to Put Even and Odd elements of a List into two Different 
# Lists 

n = int(input("Enter the number of elements: "))
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

print("Even numbers list:", even_list)
print("Odd numbers list:", odd_list)
