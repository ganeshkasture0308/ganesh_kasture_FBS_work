# 3. Create a class Shirt with members as sid,sname,type(formal etc), price and
# size(small,large etc) .Add following methods:
# g. Constructor (Support both parameterized and parameterless)
# h. Destructor
# i. ShowBook
class Shirt:
    def __init__(self, sid, sname, type, price, size):
        self.sid = sid
        self.sname = sname
        self.type = type
        self.price = price
        self.size = size

    def showShirt(self):
        print("Shirt ID:", self.sid)
        print("Shirt Name:", self.sname)
        print("Type:", self.type)
        print("Price:", self.price)
        print("Size:", self.size)
        print("////////////////////////////////////////////////////////////////////////")

shirt1 = Shirt(201, "Arrow", "Formal", 1200, "Large")
shirt2 = Shirt(202, "Levis", "Casual", 1500, "Medium")
shirt3 = Shirt(203,"Denim",  "partywear" ,3500, "small")

shirt1.showShirt()
shirt2.showShirt()
shirt3.showShirt()
