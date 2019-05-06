list_of_books =[
    {'book_name': 'Bible','book_price':30,'isbn':'6822892909'},
    {'book_name': 'Under the Veil','book_price':40,'isbn':'7090967878'},
    {'book_name': 'Ideal Team Player','book_price':20,'isbn':'5657646776'}]
"""
list_of_books.append({
        'book_name': 'Hero',
        'book_price': 40,
        'isbn': '2323232323'
    })
"""
def add_a_book(book_name,book_price,book_isbn):
    for each_book in list_of_books:
        if (book_isbn in each_book.values()):
            print("The book already exists")
            break
        else:
            list_of_books.append({'book_name':book_name,
                                  'book_price':book_price,
                                  'isbn':book_isbn})
            break

    for each_book in list_of_books:
        print(each_book)
    print("Ended the function")

add_a_book('John',30,'5857599750')
"""
for each_book in list_of_books:
    print(each_book)
"""
"""
def delete_a_book_by_ISBN(book_isbn):
    for each_book in list_of_books:
        if(book_isbn in each_book.values()):
            list_of_books.remove(each_book)

delete_a_book_by_ISBN('5657646776')

for each_book in list_of_books:
    for each_item in each_book:
        print(each_book[each_item])
"""