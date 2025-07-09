class Product:
    def __init__(self, pid, pname, p_price):
        self.pid =pid
        self.pname =pname
        self.p_price = p_price
        

    def showProduct(self):
        print("Product ID:", self.pid)
        print("product Name:", self.pname)
        print("Product Price:", self.p_price)
        print("##############################################################")

product1=Product(101,"milk bottle",35)
product2=Product(102,"notebook",50)
product3=Product(103,"pen",10)
product4=Product(104,"soap",20)

product1.showProduct()
product2.showProduct()
product3.showProduct()
product4.showProduct()