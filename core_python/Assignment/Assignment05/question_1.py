# 1. Write a program to prompt user to enter userid and password. If Id and
# password is incorrect give him chance to re-enter the credentials. Let him try 3
# times. After that program to terminate.

uid="ganesh"
passw=12345
for i in range(3):
    username=input("enter the username:")
    password=int(input("enter the password:"))
    if(uid==username and passw==password):
        print("login successfully...")
        break
    else:
        print("try again..")

else:
    print("invalid password and username.program stop")

