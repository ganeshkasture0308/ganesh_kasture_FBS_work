#syntax:
#if(condition1):
     
#line of code
#elif(condition2):
     #line of code
#else:
     #lines of code

#elif ladder
#firstexample
# n=int(input("enter the number:"))

# if(n==0):
#     print(f'{n} is a neutral.')

# elif(n>0):
#     print(f'{n} is a posituve number.')

# else:
#     print(f'{n} is a negative number.')

#secondexample
num1=int(input("enter the value of num1:"))
num2=int(input("enter the valu of num2:"))
op=input("enter operation(+,-,*,/):")
if(op=="+"):
    print("addition is:",num1+num2)
elif(op=="-"):
    print("Substraction is:",num1-num2)
elif(op=="*"):
    print("Multiplication is:",num1*num2)
elif(op=="/"):
    print("Division is:",num1/num2)
else:
    print("invalid operator....please enter valid operator!!!")


        