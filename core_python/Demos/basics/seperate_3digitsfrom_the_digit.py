#seperate out digits from thre digits
#take input from the userrs
num=int(input("enter three digits numbers:"))
d1=num%10
num=num//10
d2=num%10
num=num//10
d3=num%10
#output is
print(f"d1 is :{d1},d2 is:{d2},d3 is:{d3}")#f srtring



