from typing import Optional, Dict

booklist = [{"name": "test",
             "price": "0.99",
             "isbn": "111"},
            {"name": "test1",
             "price": "1.99",
             "isbn": "112"}]
""" Above is the list with dictionaries with single element as key value pairs"""

'''for everybook in booklist:
    for dictitem in everybook.items():
        print(dictitem[0] + " :  " + dictitem[1])'''
"""This function adds a book only if the book name  is not found in the existing book list"""

def add_a_book(_name, _price, _isbn):
    book = {'name': _name,
            'price': _price,
            'isbn': _isbn}

    if find_book_isbn(_isbn) == []:
        #print("please add the book to the list")
        booklist.append(book)
    else:
        print("Hey " + _name + " already exists.")
"""This function removes the book from the existing book list only if the book is present in the list"""

def remove_a_book(_isbn):
    book = find_book_isbn(_isbn)
    if book!= [] :
       booklist.remove(book)
       print("Removed book with "+ str(book))
    else:
        print(" Cannot remove this book, no book exists with the ISBN")

"""This book update the list if the book is found with the given name in the book list"""

def update_a_book(_name, _price):

    book = find_book_name(_name)

    if book != []:
         book['name'] = _name
         print("updated " + str(book))

"""This function update the book in the book list if the ISBN is found in the book list"""

def update_a_book(_name, _price, _isbn):

    book = find_book_isbn(_isbn)

    if book != []:
        book['name'] = _name
        book['price'] = _price
        print("updated " + str(book))


"""This function update the book in the book list if the ISBN is found in the book list"""

def update_a_book(_price, _isbn):

    book = find_book_isbn(_isbn)

    if book != None:
        book['price'] = _price
        print("updated " + str(book))

def update_a_book(_name, _price,):

    book = find_book_name(_name)
    if book != []:
       print("updated " + str(book))

def find_book_name(_name):
    book_list = []
    for everybook in booklist:
        if everybook['name'] == _name:
            book_list.append(everybook)
    return book_list

def find_book_price(_price):
    book_list = []
    for everybook in enumerate(booklist):
        if everybook['price'] == _price:
            book_list.append(everybook)
    return book_list

def find_book_name_price(_name,_price):
    book_list = []
    for everybook in enumerate(booklist):
        if everybook['name'] == _name and everybook['price'] == _price :
            book_list.append(everybook)
    return book_list

def find_book_isbn(_isbn):
    for everybook in booklist:
        if everybook['isbn'] == _isbn:
            return everybook
    return None

def get_a_book(_name, _price):
    for everybook in enumerate(booklist):
        if everybook['name'] == _name and everybook['price'] == _price:
            return everybook
    return None
def get_a_book(_name, _price):
    for everybook in enumerate(booklist):
        if everybook['name'] == _name and everybook['price'] == _price :
            return everybook
    return None

def get_all_books(_name, _price, _isbn):
    for everybook in enumerate(booklist):
        print(everybook)


def get_all_books(_name,_price,_isbn):

    book_list =[]

    if _isbn!=None and _isbn != '':
        book = find_book_isbn(_isbn)
        book_list.append(book)
    elif _name!=None and _name != ''and _price!=None and _price != '':
          filtered_book_list=find_book_name_price(_name, _price)
          book_list.extend(filtered_book_list)
    elif _name!= None and _name != '':
        filtered_book_list=find_book_name(_name)
        book_list.extend(filtered_book_list)
    elif _price!=None and _price != '':
        filtered_book_list=find_book_price(_price)
        book_list.extend(filtered_book_list)
    return book_list

book = {"name": "test4",
        "price": "4.99",
        "isbn": "114"}

book1 = {"name": "test4",
        "price": "4.99",
        "isbn": "117"}

add_a_book(book['name'],book['price'], book['isbn'])
add_a_book(book1['name'],book1['price'], book1['isbn'])

print(booklist)


#remove_a_book('117')
#print(booklist)
#print("bookname with 111 removed")"""
#update_a_book('test','8.99')
update_a_book('test','0.99')
print(get_all_books('test', None, None))
print(get_all_books('test','',''))

