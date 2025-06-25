# 3. Accept no. of passengers from user and per ticket cost. Then accept age of each
# passenger and then calculate total amount to ticket to travel for all of them based on
# following condition :
# a. Children below 12 = 30% discount
# b. Senior citizen (above 59) = 50% discount
# c. Others need to pay full.

no_passenger=int(input("enter the number of passenger:"))
ticket_price=int(input("enter the price of one ticket:"))
total_amount=0
for i in range(no_passenger):
    age=int(input(f"enter the age of the passenger{i+1}:"))
    if age<12:
        fare=ticket_price*0.70
    elif age>59:
        fare=ticket_price*0.50
    else:
        fare=ticket_price
    total_amount+=fare
print("total amount to be paid is:",total_amount,"Rs")