#8. Write a program to prompt user to enter userid and password. After verifying 
#userid and password display a 4 digit random number and ask user to enter the 
#same. If user enters the same number then show him success message otherwise failed. (Something like captcha)

import random
correct_userid="Ganesh"
correct_password=12345

userid=input("enter the userid=")
passowrd=int(input("enter the password:"))

if(userid==correct_userid and passowrd==correct_password):
    captcha=random.randint(1000,9999)
    print("captcha:",captcha)

    entered_captcha=int(input("enter the captcha:"))
    if(entered_captcha==captcha):
        print("login successfully !!!")
    else:
        print("enter the correct captcha...")

else:
    print("please enter the correct userid and password!!!")