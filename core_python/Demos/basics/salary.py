salary = int(input("Enter your salary: "))
da = salary * (10 / 100)
ta = salary * (12 / 100)
hra = salary * (15 / 100)

total_salary = salary + da + ta + hra
print("Your Da is:", da)
print("Your TA is:", ta)
print("Your HRA is:", hra)
print("Your total salary is:", total_salary)
