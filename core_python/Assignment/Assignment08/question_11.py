def get_number():
    return int(input("Enter a number: "))

def count_digits(n):
    count = 0
    temp = n
    while temp > 0:
        count += 1
        temp //= 10
    return count

def is_armstrong(n):
    power = count_digits(n)
    temp = n
    result = 0

    while temp > 0:
        digit = temp % 10
        result += digit ** power
        temp //= 10

    return result == n

def display_result(n):
    if is_armstrong(n):
        print(n, "is an Armstrong number.")
    else:
        print(n, "is not an Armstrong number.")
num = get_number()
display_result(num)
