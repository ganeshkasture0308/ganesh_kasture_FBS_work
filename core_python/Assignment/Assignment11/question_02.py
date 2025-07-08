# 2. Python Program to Merge Two Lists and Sort it
n1 = int(input("Enter number of elements in first list: "))
list1 = []
for i in range(n1):
    num = int(input(f"Enter element {i+1} for first list: "))
    list1.append(num)

n2 = int(input("Enter number of elements in second list: "))
list2 = []
for i in range(n2):
    num = int(input(f"Enter element {i+1} for second list: "))
    list2.append(num)

merged_list = list1 + list2
merged_list.sort()

print("Merged and sorted list:", merged_list)
