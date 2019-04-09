import BookStore

b = BookStore.Book()
b.addBook("Bible", 123, 60)
b.addBook("Harry Poter", 124, 50)
b.addBook("Harry Poter", 124, 50)
print(b.bookList)
b.delBook("Harry Poter")
print(b.bookList)

