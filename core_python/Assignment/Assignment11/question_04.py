n = int(input("Enter number of elements: "))
lst = []
for i in range(n):
    num = int(input(f"Enter element {i+1}: "))
    lst.append(num)

for i in range(n):
    for j in range(0, n - i - 1):
        if lst[j] > lst[j + 1]:
            lst[j], lst[j + 1] = lst[j + 1], lst[j]

print("Second largest number is:", lst[-2])
