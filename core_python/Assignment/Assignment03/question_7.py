#7. Write a program to check if user has entered correct userid and password.
correct_userid="ganesh"
correct_password=12345

userid=input("enter the user id:")
password=int(input("enter the password:"))

if(userid==correct_userid and password==correct_password):
    print("successfully login...")
else:
    print("please,enter the right userid and password")