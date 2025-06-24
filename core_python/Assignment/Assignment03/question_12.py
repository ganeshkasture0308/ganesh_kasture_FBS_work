#12. Write a program to check if given 3 digit number is a palindrome or not. 
num=input("enter the number:")
if(num==num[::-1]):
    print("it is a palindrome.")
else:
    print("it is not a palindrome.")

           #or

num=int(input("enter the number:"))
original=num
reverse=0
while num>0:
    digit=num%10
    reverse=reverse*10+digit
    num=num//10

if(original==reverse):
    print("it is a palindrome")
else:
    print("it is not a palindrome")