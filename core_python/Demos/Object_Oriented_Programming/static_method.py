####Static method
#1.class level method
#2.no self parameter
#3.Accessed using class name

class Student:
    strength=0
    def __init__(self,name,age,address):
        Student.strength+=1
        self.name=name
        self.age=age
        self.address=address

    def showData(self):
        return f"name:{self.name}\nAge:{self.age}\nAddress:{self.address}"
    
    def totalCount():
        print("Total stength:",Student.strength)

obj1=Student("ganesh kasture",22,"Latur")
print(obj1.showData())
obj2=Student("omkar kasture",23,"pune")
print(obj2.showData())
print("###########################")
Student.totalCount()