#9. Input 5 subject marks from user and display grade(eg.First class,Second class ..) 
mark1=float(input("enter the marks of the first subject="))
mark2=float(input("enter the marks of the second subject="))
mark3=float(input("enter the marks of the third subject="))
mark4=float(input("enter the marks of the forth subject="))
mark5=float(input("enter the marks of the fifth subject="))

total_marks=mark1+mark2+mark3+mark4+mark5
percentage=total_marks/5

if(percentage>=75):
    print("outstanding performance...")

elif percentage>=60 :
    print("first class")
elif percentage>=50:
    print("second class")
elif percentage>=35:
    print("pass")

else:
    print("fail in the exam")