#10.  WAP to check if given number is Perfect Number.

num = int(input("Enter a number: "))

i = 1
sum_of_divisors = 0

while i < num:
    if num % i == 0:
        sum_of_divisors += i
    i += 1

if sum_of_divisors == num:
    print(num, "is a Perfect Number.")
else:
    print(num, "is not a Perfect Number.")  