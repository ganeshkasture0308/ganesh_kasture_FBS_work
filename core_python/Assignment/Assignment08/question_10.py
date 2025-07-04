def check_leap_year(year):
    if (year % 4 == 0 ):
        print(year, "is a leap year.")
    else:
        print(year, "is not a leap year.")
yr = int(input("Enter a year: "))
check_leap_year(yr)
