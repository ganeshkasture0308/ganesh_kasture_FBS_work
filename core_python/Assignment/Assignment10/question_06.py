
numbers = [10, 20, 10, 30, 40, 20, 50, 30]

unique_list = []

for num in numbers:
    if num not in unique_list:
        unique_list.append(num)

print("List after removing duplicates:", unique_list)
