# 8. Write a program to solve the following series : 
# a. 1! + 2! + 3! + 4! + …..n! 
# b. N + N^2 + N^3+N^4 …..+N^N (here ^ means exponent) 
# c. Find the sum of a geometric series from 1 to n where the common ratio is 2. 
# d. S = a + a2 / 2 + a3 / 3 + …… + a10 / 10 
# e. x - x2/3 + x3/5 - x4/7 + …. to n terms 

#a.sum of factorials
# a. 1! + 2! + 3! + 4! + …..n!

n = int(input("Enter the value of n: "))
i = 1
sum = 0

while i <= n:
    fact = 1
    j = 1
    while j <= i:
        fact *= j
        j += 1
    sum += fact
    i += 1

print("Sum of factorials is:", sum)


