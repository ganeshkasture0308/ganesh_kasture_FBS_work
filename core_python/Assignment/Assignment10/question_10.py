num=int(input("enter numbers of elements: "))

number=[]

for i in range(num):
    num = int(input(f"Enter element {i+1}: "))
    number.append(num)

to_remove = int(input("Enter the element to remove: "))

updated_list = []
for num in number:
    if num != to_remove:
        updated_list.append(num)

print("Original List:", number)
print("Updated List (after removal):", updated_list)
