#4. Write a program to input all sides of a triangle and check whether triangle is valid or not.
a=int(input("ente the first side:"))
b=int(input("enter the second side:"))
c=int(input("enter the third side:"))

if((a+b>c)and(a+c>b)and(b+c>a)):
    print("it is a valid triangle.")
else:
    print("it is a not valid triangle.")
