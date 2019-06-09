import BookStore

b = BookStore.Books()
b.add_a_book(name="Bible", price=50, isbn= 123)
b.add_a_book(name="Harry Poter", price=20, isbn=124)
b.add_a_book(name="Harry Poter", price=24, isbn=124)
b.remove_a_book(name="Harry Poter")
print(b.bookList)

