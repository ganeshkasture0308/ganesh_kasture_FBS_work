
radius = 20
length = 50
breadth = 40
cost_per_meter = 35
circle_part = 3.14 * radius
rectangle_part = 2 * (length + breadth)


total_perimeter = circle_part + rectangle_part


total_fencing_length = total_perimeter * 5


total_cost = total_fencing_length * cost_per_meter

print("Total fencing cost: ₹",(total_cost, 2))
