#6. WAP to calculate total salary of employee based on basic, da=10% of basic, 
#ta=12% of basic, hra=15% of basic.
basic_salary=float(input("enter the basic salary of the employee:"))
da=(10/100)*basic_salary
ta=(12/100)*basic_salary
hra=(15/100)*basic_salary
total_salary=basic_salary+da+ta+hra
print(f'total salary of the employee is:{total_salary}rs')

