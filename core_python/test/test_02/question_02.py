#Write a program to accept 3 digit number. If first digit is double of second digit and half of 
#third digit then display “Yes, you have done it”, otherwise display “Please try next time”. 
#Eg : -  428   ,  214 etc.
num=int(input("enter the number:"))
first_number=num//100
second_number=(num//10)%10
third_number=num%10
if(first_number==2*second_number and first_number*2==third_number):
    print("Yes, you have done it!")
else:
    print("Please try next time!")

