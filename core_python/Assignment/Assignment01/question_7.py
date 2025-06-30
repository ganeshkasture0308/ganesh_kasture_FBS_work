#7.Program to Find the Roots of a Quadratic Equation.this program is direct taken through the chatgpt.
import math

# Input coefficients
a = float(input("Enter coefficient a: "))
b = float(input("Enter coefficient b: "))
c = float(input("Enter coefficient c: "))

# Calculate discriminant
d = b**2 - 4*a*c

# Check the nature of roots
if d > 0:
    root1 = (-b + math.sqrt(d)) / (2*a)
    root2 = (-b - math.sqrt(d)) / (2*a)
    print("Roots are real and different.")
    print("Root 1 =", root1)
    print("Root 2 =", root2)
elif d == 0:
    root = -b / (2*a)
    print("Roots are real and equal.")
    print("Root =", root)
else:
    real = -b / (2*a)
    imag = math.sqrt(-d) / (2*a)
    print("Roots are complex and imaginary.")
    print("Root 1 = {:.2f} + {:.2f}i".format(real, imag))
    print("Root 2 = {:.2f} - {:.2f}i".format(real, imag))
