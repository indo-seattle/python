# Book.py

list_of_books = [{
        'name': 'The Bible',
        'price':'0.99',
        'ISBN':'111111'
    },
    {
        'name': 'The Life and Legacy',
        'price': '1.99',
        'ISBN': '111112'
    }
]

# books.append(
#                 {
#                     'name': 'The Economics of USA',
#                     'price':'2.99',
#                     'ISBN':'111113'
#                 }
#             )
# #print(books)
# for each_book in books:
#     #print(each_book)
#     for each_item in each_book:
#         print(each_item, each_book[each_item])



def add_a_book(name, price, ISBN):
    list_of_books.append({
        'name':name,
        'price':price,
        'ISBN':ISBN
    })

def delete_a_book_by_ISBN(ISBN):
    for each_book in list_of_books:
        if (ISBN in each_book.values()):
            list_of_books.remove(each_book)



add_a_book('The ISCF Passion', '0.98', '111123')
delete_a_book('111123')
print(list_of_books)











