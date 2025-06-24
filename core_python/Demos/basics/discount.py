p1 = int(input("Enter the price of the first item: "))
p2 = int(input("Enter the price of the second item: "))
p3 = int(input("Enter the price of the third item: "))
p4 = int(input("Enter the price of the fourth item: "))
p5 = int(input("Enter the price of the fifth item: "))

total_amt= p1 + p2 + p3 + p4 + p5

discount = total_amt * (10/100)

final_amt = total_amt - discount

print("Total amount: ", total_amt)
print("Discount amount:", discount)
print("Final amount after discount:", final_amt)