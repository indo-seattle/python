# list_book = [{'Name':'Lord of the rings - 1', 'Price': '$10.99', 'ISBN': '01'}]
# list_book.append({'Name':'Lord of the rings - 2', 'Price': '$20.99', 'ISBN': '02'})
# list_book.append({'Name':'Lord of the rings - 3', 'Price': '$30.99', 'ISBN': '03'})
#
# for eachbook in list_book:
#     for eachitem in eachbook:
#         print(eachitem, eachbook[eachitem])

# list_of_books = []
# def add_a_book(name, price, ISBN):
#
#
#     list_of_books.append({'name': book_name, 'book_price': book_price, 'book_isbn': book_isbn})
#
# for eachbook in list_book:
#     for eachitem in eachbook:
#         print(eachitem, eachbook[eachitem])
#
# add_a_book(book_name, book_price, book_isbn)

### Add and delete book
# list_of_books = [{'name': 'book1', 'price': '$1', 'ISBN': '1'}]
#
# def add_a_book(name, price, ISBN):
#     list_of_books.append({'name': name, 'price': price, 'ISBN': ISBN})
#
# add_a_book('The ISCF', '098', '123')

list_of_books = []


def add_a_book(name, price, ISBN):
    list_of_books.append({'name': name, 'price': price, 'ISBN': ISBN})


can_continue = True

while can_continue == True:
    book_name = input("Enter Book Name: ")
    book_price = input("Enter price: ")
    book_isbn = input("Enter ISBN: ")

    add_a_book(book_name, book_price, book_isbn)
    quest_continue = input("Do you want to continue (Y/N): ")
    # if quest_continue == 'N':
    #     can_continue = False
    # elif quest_continue == 'Y':
    #     can_continue = True
    if quest_continue == 'N':
        can_continue = False
    elif quest_continue == 'Y':
        can_continue = True
    else:
        quest_continue = input("Please only enter (Y/N): ")
        if quest_continue == 'N':
            can_continue = False
        elif quest_continue == 'Y':
            can_continue = True

print(list_of_books)


def delete_a_book(ISBN):
    for each_book in list_of_books:
        if ISBN in each_book.values():
            if each_book in list_of_books:
                list_of_books.remove(each_book)


delete_a_book('1')
#
print(list_of_books)
