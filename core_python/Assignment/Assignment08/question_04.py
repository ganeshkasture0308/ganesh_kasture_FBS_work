def sum_of_odds(n):
    total = 0
    for i in range(1, n + 1):
        if i % 2 != 0:
            total += i
    return total

# Input from user
num = int(input("Enter the value of n: "))
result = sum_of_odds(num)
print("Sum of odd numbers from 1 to", num, "is:", result)
