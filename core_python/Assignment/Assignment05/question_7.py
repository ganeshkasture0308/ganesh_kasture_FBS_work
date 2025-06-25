# 7. Write a program to print first n prime numbers. 
n = int(input("Enter how many prime numbers to print: "))

count = 0       
num = 2         
print("First", n, "prime numbers are:")

while count < n:
    is_prime = True
    i = 2

    while i < num:
        if num % i == 0:
            is_prime = False
            break
        i += 1

    if is_prime:
        print(num, end=" ")
        count += 1

    num += 1
