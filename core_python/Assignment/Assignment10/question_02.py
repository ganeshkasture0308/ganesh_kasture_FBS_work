# 2. Write a program to find maximum and minimum element in a list.
numbers = [10, 25, 7, 99, 3]
maximum = numbers[0]
minimum = numbers[0]
for num in numbers[1:]:
    if num > maximum:
        maximum = num
    if num < minimum:
        minimum = num
print("Maximum element:", maximum)
print("Minimum element:", minimum)
