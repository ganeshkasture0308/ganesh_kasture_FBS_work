#Geometric Series (1 to n, ratio = 2):
# #Find the sum of a geometric series from 1 to n where the common ratio is 2.
n = int(input("Enter number of terms: "))
i = 0
term = 1
sum = 0

while i < n:
    sum += term
    term *= 2
    i += 1

print("Sum of geometric series:", sum)
