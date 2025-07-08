# 3. Python Program to Sort the List According to the Second Element in Sublist
n = int(input("Enter number of sublists: "))
sublists = []

for i in range(n):
    a = int(input(f"Enter first element of sublist {i+1}: "))
    b = int(input(f"Enter second element of sublist {i+1}: "))
    sublists.append([a, b])

sublists.sort(key=lambda x: x[1])

print("Sorted list based on second element:", sublists)
