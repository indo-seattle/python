class ValueTooSmallError:
    """Raised when the input value is too small"""
    pass


class Book:
    def __init__(self):
        self.book = {}
        self.bookList = []

    def addBook(self, name, isbn, price):
        try:
            if self._find(name, isbn) == None:
                self.book.update(Name = name)
                self.book.update(ISBN = isbn)
                self.book.update(Price = price)
                self.bookList.append(self.book)
            else:
                raise Exception("Book Name or ISBN already exists")
        except Exception as err:
            print(err)

    def _find(self, name=None, isbn=None):
        for index in range(0, len(self.bookList)):
            self.book = self.bookList[index]
            if (name in self.book.values()) or (isbn in self.book.values()):
                return index
            else:
                return None
        return None

    def delBook(self, name=None, isbn=None):
        try:
            index = self._find(name, isbn)
            if index == None:
                raise Exception("Book Name or ISBN does not exists")
            else:
                self.bookList.pop(index)
        except Exception as err:
            print(err)








