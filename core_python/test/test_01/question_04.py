
def calculate_painting_cost():
    print("Enter the areas in square feet and costs per square foot.")

    interior_area = float(input("Enter total interior wall area: "))
    interior_cost_per_sqft = float(input("Enter cost per square foot for interior painting: "))

    exterior_area = float(input("Enter total exterior wall area: "))
    exterior_cost_per_sqft = float(input("Enter cost per square foot for exterior painting: "))

    total_interior_cost = interior_area * interior_cost_per_sqft
    total_exterior_cost = exterior_area * exterior_cost_per_sqft
    total_cost = total_interior_cost + total_exterior_cost
 
    print("\n--- Painting Cost Details ---")
    print(f"Total Interior Painting Cost: ₹{total_interior_cost:.2f}")
    print(f"Total Exterior Painting Cost: ₹{total_exterior_cost:.2f}")
    print(f"Total Painting Cost: ₹{total_cost:.2f}")

calculate_painting_cost()
