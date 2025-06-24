# 3. Accept no. of passengers from user and per ticket cost. Then accept age of each
# passenger and then calculate total amount to ticket to travel for all of them based on
# following condition :
# a. Children below 12 = 30% discount
# b. Senior citizen (above 59) = 50% discount
# c. Others need to pay full.

no_passengers=int(input("enter the number of passenger:"))
ticket_price=int(input("enter the price of the one ticket:"))
i=0
fare=0
while i<no_passengers:
    age=int(input("enter the age of the passengers:"+str(i+1)+": "))
    if age<12:
        fare=ticket_price*0.70
    elif age>59:
        fare=ticket_price*0.50
    else:
        ticket_price+=fare
    i+=1
print(f"\ntotal ticket amount for all passengers:Rs.",total_amount)