#superclass

class Person:
    def __init__(self,name,age,address):
        self.name=name
        self.age=age
        self.address=address

    def display(self):
        print("Name:",self.name)
        print("Age:",self.age)
        print("Address:",self.address)

class Student(Person):
    def __init__(self,name,age,address,course):
        super().__init__(name,age,address)
        self.course=course

    def display(self):
        super().display()
        print("Course:",self.course)

std1=Student("Ganesh kasture",22,"Latur","Python Data Science")
std1.display()
