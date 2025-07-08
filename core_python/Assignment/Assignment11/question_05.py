n = int(input("Enter number of elements: "))
lst = []
for i in range(n):
    element = input(f"Enter element {i+1}: ")
    lst.append(element)

lst.sort(key=len)
print("Sorted list by length:", lst)
