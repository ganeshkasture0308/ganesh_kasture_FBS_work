def count_digits(n):
    if n == 0:
        return 0
    return 1 + count_digits(n // 10)
def armstrong_sum(n, power):
    if n == 0:
        return 0
    digit = n % 10
    return (digit ** power) + armstrong_sum(n // 10, power)
num = int(input("Enter a number: "))
power = count_digits(num)
total = armstrong_sum(num, power)

if total == num:
    print(num, "is an Armstrong number.")
else:
    print(num, "is not an Armstrong number.")
