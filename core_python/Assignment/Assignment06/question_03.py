
rows = 4
for i in range(1, rows + 1):
    print(" " * (rows - i), end="") 
    for j in range(1, i + 1):
        if j == 1 or j == i:
            print("1", end=" ")
        else:
            print(i - 1, end=" ")
    print()
