# 11. Accept age of five people and also per person ticket amount and then calculate total 
# amount to ticket to travel for all of them based on following condition : 
# a. Children below 12 = 30% discount 
# b. Senior citizen (above 59) = 50% discount 
# c. Others need to pay full.

ticket_price=float(input("enter the price of ticket per person:"))

age1=int(input("enter the age of person 1:"))
if(age1<12):
    amt1=ticket_price*(30/100)
elif(age1<59):
    amt1=ticket_price*(50/100)
else:
    amt1=ticket_price

age2=int(input("enter the age of person 2:"))
if(age2<12):
    amt2=ticket_price*(30/100)
elif(age2<59):
    amt2=ticket_price*(50/100)
else:
    amt2=ticket_price

age3=int(input("enter the age of person 3:"))
if(age3<12):
    amt3=ticket_price*(30/100)
elif(age3<59):
    amt3=ticket_price*(50/100)
else:
    amt3=ticket_price

age4=int(input("enter the age of person 4:"))
if(age4<12):
    amt4=ticket_price*(30/100)
elif(age4<59):
    amt4=ticket_price*(50/100)
else:
    amt4=ticket_price

age5=int(input("enter the age of person 5:"))
if(age5<12):
    amt5=ticket_price*(30/100)
elif(age5<59):
    amt5=ticket_price*(50/100)
else:
    amt5=ticket_price

total_amount=amt1+amt2+amt3+amt4+amt5

print("total amount of ticket to travel all of 5 person is:",total_amount)
