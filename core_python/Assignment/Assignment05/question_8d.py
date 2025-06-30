#  S = a + a2 / 2 + a3 / 3 + …… + a10 / 10 
a = float(input("Enter the value of a: "))
i = 1
sum = 0

while i <= 10:
    sum += (a**i) / i
    i += 1

print("Sum of the series is:", sum)
