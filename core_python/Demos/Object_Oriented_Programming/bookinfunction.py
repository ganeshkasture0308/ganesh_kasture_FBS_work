class Book:
    def bookData(self,bookname,booktype,authorname,price):
        self.bookname=bookname
        self.booktype=booktype
        self.authorname=authorname
        self.price=price
    
    def display(self):
        print("bookname:",self.bookname)
        print("booktype:",self.booktype)
        print("authorname:",self.authorname)
        print("price:",self.price)
        print("############################################")

book1=Book()
book2=Book()
book3=Book()

book1.bookData(" It","Horror","Stephen King",560)
book2.bookData("The Diary of a Young Girl","Biography","Anne Frank",550)
book3.bookData("Pride and Prejudice"," Romantic","Jane Austen",350)

book1.display()
book2.display()
book3.display()