def power(m, n):
    if n == 0:
        return 1
    else:
        return m * power(m, n - 1)
base = int(input("Enter base (m): "))
exponent = int(input("Enter exponent (n): "))
print(f"{base}^{exponent} =", power(base, exponent))
