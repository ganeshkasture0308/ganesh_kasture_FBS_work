length = float(input("Enter wall length (in meters): "))
height = float(input("Enter wall height (in meters): "))
cost_per_sqft = float(input("Enter painting cost per square meter: "))

area = 4 * length * height

cost = area * cost_per_sqft

print("Total painting cost: ₹", (cost, 2))
