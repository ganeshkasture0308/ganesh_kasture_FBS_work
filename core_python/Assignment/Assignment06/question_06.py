rows = 5
for i in range(rows):
    print(" " * (rows - i - 1), end="")
    for j in range(1, 2 * i + 2):
        print(j, end="") 
    print()
