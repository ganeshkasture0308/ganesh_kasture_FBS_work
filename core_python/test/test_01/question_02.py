#2. Write a program to calculate simple interest based on
#Principal, Rate and Time (SI = P*R*T/100)

principle=int(input("enter the principle:"))
rate=int(input("enter the rate:"))
time=int(input("enter the years:"))

simple_interest=(principle*rate*time)/100
print("simple interest is:",simple_interest)