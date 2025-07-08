#  A man goes for shopping. He buys 5 products. Accept the price of all products and display 
# the total bill after adding 18% GST

total = 0
for i in range(1, 6):
    price = float(input(f"Enter price of product {i}: "))
    total += price

gst = total * 0.18
final_amount = total + gst

print("Total bill with 18% GST: ₹", round(final_amount, 2))
