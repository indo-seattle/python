class Book:
    def __init__(self):
        self.book = {}
        self.bookList = []

    def addBook(self, name, isbn, price):
        self.book.update(Name = name)
        self.book.update(ISBN = isbn)
        self.book.update(Price = price)
        self.bookList.append(self.book)


