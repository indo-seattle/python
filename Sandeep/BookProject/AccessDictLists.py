list_of_books =[
    {'book_name': 'Bible','book_price':30,'book_isbn':'6822892909'},
    {'book_name': 'Under the Veil','book_price':40,'book_isbn':'7090967878'},
    {'book_name': 'Ideal Team Player','book_price':20,'book_isbn':'5657646776'}]

for each_book in list_of_books:
    for each_item in each_book:
        print(each_book[each_item])


for each_book in list_of_books:
    for each_item in each_book:
        print(each_book.values())


