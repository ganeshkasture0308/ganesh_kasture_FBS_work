###Constructor:
#1.Special method,called automatically when object of that class is created.
#2.use __init__ as the function name.
#3.We pass parameters to constructor in the time of object creating.

class Student:
    def __init__(self,roll_no,name,course,address):
        self.roll_no=roll_no
        self.name=name
        self.course=course
        self.address=address

    def display(self):
        print("Roll No:",self.roll_no)
        print("Name:",self.name)
        
        print("course:",self.course)
        print("address:",self.address)
        print("########################")

s1=Student(1,"Sujit Wayker","Core python","Manchar")
s1.display()
s2=Student(2,"Ganesh kasture","Data Science","Latur")
s2.display()