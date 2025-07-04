def generate_fibonacci():
    n = int(input("Enter the number of terms: "))
    a, b = 1, 1
    count = 0
    result = ""
    while count < n:
        result += str(a) + " "
        a, b = b, a + b
        count += 1
    return result
series = generate_fibonacci()
print("Fibonacci series:")
print(series)
