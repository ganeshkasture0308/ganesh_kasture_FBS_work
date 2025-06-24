# 2. Enter number of students from user. For those many students accept marks of 5  
# subject marks from user and calculate percentage. Display all percentage and  
# average percentage of students. 

num_student=int(input("enter the number of student:"))
i=0
total_percent=0
while i<num_student:
    print(f"\nenter marks of 5 subjects of student{i+1}:")
    s1=float(input("\nenter the marks of first subject:"))
    s2=float(input("enter the marks of second subject:"))
    s3=float(input("enter the marks of third subject:"))
    s4=float(input("enter the marks of forth subject:"))
    s5=float(input("enter the marks of fifth subject:"))
    total=s1+s2+s3+s4+s5
    percentage=(total/500)*100
    total_percent+=percentage
    print(f"\npercentage of student{i+1}:{percentage}%")
    i+=1
average=total_percent/num_student
print(f"\nAverage percentage of all student is:{average}%")