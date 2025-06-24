#5. Write a program to check whether the triangle is equilateral, isosceles or scalene triangle. 
a=float(input("enter the  first side of the triangle:"))
b=float(input("enter the second side of the triangle:"))
c=float(input("enter the third side of the triangle:"))

if((a+b>c)and(a+c>b)and(b+c>a)):
    if(a==b==c):
        print("it is a equilateral triangle.")
    elif (a==b)or(b==c)or(a==c):
        print("it is a isosceles triangle.")
    else:
        print("it is a scalene triangle.")

else:
    print("it is not a valid triangle.")