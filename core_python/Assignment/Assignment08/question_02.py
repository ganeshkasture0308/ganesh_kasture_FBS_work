# 2. Write a program to calculate area of circle 
#with passing parameter /argument with returing values.
def area_circle(radius):
    area=3.14*radius*radius
    return area

r=int(input("enter the radius:"))
result=area_circle(r)
print("Area of the circle is:",result)
    