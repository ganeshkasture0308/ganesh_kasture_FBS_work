#  x - x2/3 + x3/5 - x4/7 + …. to n terms 
x = float(input("Enter the value of x: "))
n = int(input("Enter number of terms: "))

i = 1
sign = 1
den = 1
sum = 0

while i <= n:
    term = (x**i) / den
    sum += sign * term
    sign *= -1  # alternate sign
    i += 1
    den += 2

print("Sum of the alternating series:", sum)
