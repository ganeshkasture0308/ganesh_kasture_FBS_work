#from file_name import class_name
from shape import Shape

class Rectangle(Shape):
    def __init__(self, id, area, length, breadth):
        super().__init__(id, area)
        self.l = length
        self.b = breadth
    
    def display(self):
        super().display()
        print("Length:", self.l)
        print("Breadth:", self.b)

rect1 = Rectangle('rect1', 800, 40, 20)
rect1.display()