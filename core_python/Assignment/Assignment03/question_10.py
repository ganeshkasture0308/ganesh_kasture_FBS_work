#10. Write a program to check if person is eligible to marry or not (male age >=21 and female age>=18) 
gender=input("enter the gender (male/female)=").lower()
age=int(input("enter the age="))
if(gender=="male"):
    if(age>=21):
        print("eligible for marriage..")
    else:
        print("not eliglible for marriage.male must be 21 years old.")
elif(gender=="female"):
    if(age>=18):
        print("eligible for marriage..")
    else:
        print("not eligible for marriage.female must be atleast 18 years old..")
else:
    print("Invalid gender.please enter the right gender..")