year=int(input("enter the year:"))
if(year%4==0):
    if(year%100==0):
        if(year%400==0):
            print("leap year")
        else:
            print("not a leap year.")
    else:
        print("leap year")
else:
    print("not a leap year")


#or

year = int(input("Enter a year: "))

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("It is a leap year.")
else:
    print("It is not a leap year.")
