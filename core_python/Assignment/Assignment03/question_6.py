#6. Write a program to calculate profit or loss.
cost_price=int(input("enter the cost price is:"))
selling_price=int(input("enter the selling price is:"))

if(selling_price>cost_price):
    profit=selling_price-cost_price
    print("the profit is:",profit)
elif (cost_price>selling_price):
    loss=cost_price-selling_price
    print("the loss is:",loss)
else:
    print("no loss ,no profit")