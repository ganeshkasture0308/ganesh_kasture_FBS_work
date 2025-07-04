class Vehicle:
    def car(self,model,brand,price):
      print("vehcile management!!")
      self.model=model
      self.brand=brand
      self.price=price

car1=Vehicle()
car2=Vehicle()
car3=Vehicle()

car1.car(1045,"BMW",500000)
car2.car(4567,"Tata",450000)

print(car1.price)
print(car2.brand)