#11. Write a program to accept an integer amount from user and tell minimum 
#number of notes needed for representing that amount. 
# Input the total amount
amount = int(input("Enter the amount: "))


denominations = [2000, 500, 200, 100, 50, 20,10]


for note in denominations:
    count = amount // note
    if count > 0:
        print(f"{note} x {count} = {note * count}")
        amount = amount % note
