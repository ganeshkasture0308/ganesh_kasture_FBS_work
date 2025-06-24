#12. WAP to print Armstrong number within a given range

start = int(input("Enter the start of range: "))
end = int(input("Enter the end of range: "))

print("Armstrong numbers from", start, "to", end, "are:")

num = start
while num <= end:
    
    temp = num
    sum_of_powers = 0

    
    num_digits = len(str(num))


    while temp > 0:
        digit = temp % 10
        sum_of_powers += digit ** num_digits
        temp //= 10


    if sum_of_powers == num:
        print(num, end=" ")

    num += 1