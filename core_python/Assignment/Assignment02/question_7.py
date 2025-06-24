#7. Find the sum of three-digit number.
num=int(input("enter the three digits number="))
hundreds=num//100
tens=(num//10)%10
ones=num%10

sum_digits=hundreds+tens+ones
print(f'the sum of {num} is:{sum_digits}')