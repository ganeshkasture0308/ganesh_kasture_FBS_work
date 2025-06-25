# 4. Write a program to check if given number is Armstrong number or not.  
# (Hint : 153 = 1*1*1 + 5*5*5 + 3*3*3 , 1634 = 1*1*1*1 + 6*6*6*6 + 3*3*3*3 +  
# 4*4*4*4) 
num = int(input("Enter a number: "))
original_num = num
sum = 0

# Count the number of digits
digits = 0
temp = num
while temp > 0:
    temp = temp // 10
    digits += 1

# Calculate sum of powers of digits
temp = num
while temp > 0:
    digit = temp % 10
    sum += digit ** digits
    temp = temp // 10

# Check if Armstrong
if sum == original_num:
    print(original_num, "is an Armstrong number.")
else:
    print(original_num, "is not an Armstrong number.")
