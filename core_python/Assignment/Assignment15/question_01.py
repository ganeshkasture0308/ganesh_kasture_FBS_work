# 1. Create a class Book with members as bid,bname,price and author.Add following
# methods:
# a. Constructor (Support both parameterized and parameterless)
# b. Destructor
# c. ShowBook
class Book:
    def __init__(self, bid, bname, price, author):
        self.bid = bid
        self.bname = bname
        self.price = price
        self.author = author

    def showBook(self):
        print("Book ID:", self.bid)
        print("Book Name:", self.bname)
        print("Price:", self.price)
        print("Author:", self.author)
        print("##############################################################")

book1 = Book(101, "It", 560, "Stephen King")
book2 = Book(102, "The Diary of a Young Girl", 550, "Anne Frank")
book3 = Book(103,"Pride and Prejudice",450,"Jane Austen") 

book1.showBook()
book2.showBook()
book3.showBook()
