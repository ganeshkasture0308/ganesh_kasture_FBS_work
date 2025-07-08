###Destructor
#1.Special method  called automatically when life cycle of the object is completed.
    #or when we are deleting the objects.
#2.Basically used for closing below resources.
   #files
   #networks ports
   #Database
#3.use __del__ aas name of a destructor.

class Person:
    def __init__(self,name,address,age):
        self.nm=name
        self.add=address
        self.age=age
    def showData(self):
        print("Name:",self.nm)
        print("Address:",self.add)
        print("Age:",self.age)
    def __del__(self):
        print("Destructor is called.")
p1=Person("ABC","Pune",24)
del p1
#p1.showData()