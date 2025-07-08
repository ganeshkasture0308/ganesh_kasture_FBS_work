from shape import Shape

class Circle(Shape):
    def __init__(self, id, area, radius):
        super().__init__(id, area)
        self.r = radius
    
    def display(self):
        super().display()
        print("Radius:", self.r)

c1 = Circle("Cir01", 314, 10)
c1.display()