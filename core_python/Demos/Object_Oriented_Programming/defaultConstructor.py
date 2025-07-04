class Animal:
    def __init__(self,name="Dog",type="Pet",color="Black",gender="Male"):
        self.name=name
        self.type=type
        self.color=color
        self.gender=gender

    def getData(self):
        data=(f"Name:{self.name}\nType:{self.type}\nColor:{self.color}\nGender{self.gender}")
        return data
    
cat=Animal("Cat","Pet","Black","Female")
print(cat.getData())
print("####################################")
a1=Animal()
print(a1.getData())