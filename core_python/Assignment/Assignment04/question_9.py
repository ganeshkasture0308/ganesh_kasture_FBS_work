#9. WAP to print all numbers in a range divisible by a given number.

start = int(input("Enter the start of range: "))
end = int(input("Enter the end of range: "))
divisor = int(input("Enter the number to divide by: "))

print(f"Numbers from {start} to {end} divisible by {divisor} are:")

for i in range(start, end + 1):
    if i % divisor == 0:
        print(i, end=" ") 