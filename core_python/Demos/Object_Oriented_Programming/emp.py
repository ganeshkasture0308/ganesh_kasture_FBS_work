###Implementations of class
class Employee:
    def setData(self,id,name,sal):#methods/behaviour
        print("This is a setData Method.")
        print("This ia setData Method.")
        self.id=id
        self.ename=name
        self.ssal=sal


####Creating of object
#object_name=class_name()
emp1=Employee()
emp2=Employee()


####Calling behaviour/method
#obj_name.function_name()
emp1.setData(101,"Akshya Kumar",50000)
emp2.setData(102,"Salman Khan",60000)
print(emp1.ename)

