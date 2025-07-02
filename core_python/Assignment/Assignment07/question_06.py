rows = 5
for i in range(1, rows + 1):
    for j in range(1, rows + 1):
        if i == 1:  
            print(j, end=" ")
        elif j == i or j == rows: 
            print(j, end=" ")
        else:
            print("  ", end="")  
    print()
