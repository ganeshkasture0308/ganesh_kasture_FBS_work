#3. Write a program to input angles of a triangle and check whether triangle is valid or not. 
angle1=float(input("enter angle 1="))
angle2=float(input("enter angle 2="))
angle3=float(input("enter angle 3="))

sum_of_angles=angle1+angle2+angle3

if(sum_of_angles==180 and angle1>0 and angle2>0 and angle3>0):
    print("it is a valid triangle.")

else:
    print("it is not a valid triangle.")