class Book:
    def bookData(self,bookname,booktype,authorname,price):
        self.bookname=bookname
        self.booktype=booktype
        self.authorname=authorname
        self.price=price

book1=Book()
book2=Book()
book3=Book()

book1.bookData(" It","Horror","Stephen King",560)
book2.bookData("The Diary of a Young Girl","Biography","Anne Frank",550)
book3.bookData("Pride and Prejudice"," Romantic","Jane Austen",350)

print(book1.bookname)
print(book2.booktype)