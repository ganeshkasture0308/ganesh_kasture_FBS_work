
numbers = [10, 20, 30, 20, 40, 50, 20]

n = int(input("Enter a number to search: "))

count = 0
for num in numbers:
    if num == n:
        count += 1

if count > 0:
    print(f"The number {n} is present {count} time(s) in the list.")
else:
    print(f"The number {n} is not present in the list.")
