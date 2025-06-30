#Sum of Powers:
#b. N + N^2 + N^3+N^4 …..+N^N (here ^ means exponent)
N = int(input("Enter the value of N: "))
i = 1
sum = 0

while i <= N:
    sum += N**i
    i += 1

print("Sum of N powers:", sum)
