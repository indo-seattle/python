# Book.py

# book data structure
list_of_books = [{
        'name': 'The Bible',
        'price':'0.99',
        'ISBN':'111111'
    },
    {
        'name': 'The Life and Legacy',
        'price': '1.99',
        'ISBN': '111112'
    },
    {
        'name': 'The Life and Legacy',
        'price': '1.99',
        'ISBN': '111113'
    }
]


# add_a_book(_name, _price, _ISBN): Add the book to the book list.
# Validations: do not add if the book already exists with same ISBN.
# Errors: Cannot add this book, a book already exists with the ISBN.
# Allow: Multiple books can be with the same name.
def add_a_book(_name, _price, _isbn):
    book_exists = False
    for each_book in list_of_books:
        if _isbn in each_book.values():
            raise Exception("Book already exists")

    list_of_books.append({
        'name': _name,
        'price': _price,
        'ISBN': _isbn
    })


# helper function to check if book exists by name
def is_book_exists_by_name(_name):
    for each_book in list_of_books:
        if _name in each_book.values():
            return True
    return False


# helper function to check if book exists by isbn
def is_book_exists_by_isbn(_isbn):
    for each_book in list_of_books:
        if _isbn in each_book.values():
            return True
    return False


# helper function to remove a book by isbn
def remove_a_book_by_isbn(_isbn):
    for each_book in list_of_books:
        if _isbn in each_book.values():
            list_of_books.remove(each_book)


# helper function to update a book price by name
def update_a_book_price_by_name(_name, _price):
    for each_book in list_of_books:
        if _name in each_book.values():
            each_book["price"] = _price


# helper function to update a book price by isbn
def update_a_book_price_by_isbn(_isbn, _price):
    for each_book in list_of_books:
        if _isbn in each_book.values():
            each_book["price"] = _price


# helper function to return a book by isbn
def get_a_book_by_isbn(_isbn):
    for each_book in list_of_books:
        if _isbn in each_book.values():
            return each_book


# helper function to return a book price by name
def get_a_book_by_name(_name):
    for each_book in list_of_books:
        if _name in each_book.values():
            return each_book


# helper function to return all books by name
def get_all_books_by_name(_name):
    books_found = []
    for each_book in list_of_books:
        if _name in each_book.values():
            books_found.append(each_book)
    return books_found


# helper function to return a book price by name and price
def get_a_book_by_name_and_price(_name, _price):
    for each_book in list_of_books:
        if _name in each_book.values() and _price in each_book.values():
            return each_book


# helper function to return all books price and name
def get_all_books_by_name_and_price(_name, _price):
    books_found = []
    for each_book in list_of_books:
        if _name in each_book.values() and _price in each_book.values():
            books_found.append(each_book)
    return books_found


# helper function to return all books by price
def get_all_books_by_price(_price):
    books_found = []
    for each_book in list_of_books:
        if _price in each_book.values():
            books_found.append(each_book)
    return books_found


# helper function to return a book price by price
def get_a_book_by_price(_price):
    for each_book in list_of_books:
        if _price in each_book.values():
            return each_book


# helper function to return number of books by name
def number_of_books_by_name(_name):
    count = 0
    for each_book in list_of_books:
        if _name in each_book.values():
            count += 1
    return count


# helper function to return number of books by price
def number_of_books_by_price(_price):
    count = 0
    for each_book in list_of_books:
        if _price in each_book.values():
            count += 1
    return count


# helper function to return no. of books by name and price
def number_of_books_by_name_and_price(_name, _price):
    count = 0
    for each_book in list_of_books:
        if _price in each_book.values() and _name in each_book.values():
            count += 1
    return count


# to delete a book by isbn
def delete_a_book_by_isbn(_isbn):
    if is_book_exists_by_isbn(_isbn):
        remove_a_book_by_isbn(_isbn)
    else:
        raise Exception("No book exists with the ISBN", _isbn)


# Test add_a_book
# print(list_of_books)
# add_a_book('The ISCF Passion', '0.98', '111115')
# add_a_book('The ISCF Passion', '0.98', '111116')
# print(list_of_books)
# add_a_book('The ISCF Passion', '0.98', '111111')

# test delete a book by isbn
# print(list_of_books)
# print(is_book_exists('111111'))
# delete_a_book_by_isbn('111111')
# print(list_of_books)
# delete_a_book_by_isbn('111117')
# print(list_of_books)

# update_a_book(_name, _price, _ISBN): Update an existing book.
# User input: You may not data for all three parameters always. Deal with what you get.
# Validations: If user sends only name and price, update price information for the book with the same name.
#               If you find more than one book with the name, do not update.
# Validations: If user sends ISBN, name and price, update name and price information for the book with the ISBN.
# Validations: If user sends only ISBN and price, update price information for the book with the same ISBN.
# Validations: If user sends only name or price, do not update anything.
#               Return Error saying you need at two paramenters input to perform any operation
def update_a_book(_name, _price, _isbn):
    # getting all three values
    if _name != "" and _price != "" and _isbn != "":
        if is_book_exists_by_isbn(_isbn):
            remove_a_book_by_isbn(_isbn)
            list_of_books.append({"name": _name, "price": _price, "isbn": _isbn})
        pass
    # if you get only name and price, not isbn - update price info for that book
    elif _name != "" and _price != "" and _isbn == "":
        if is_book_exists_by_name(_name):
            if number_of_books_by_name(_name) == 1:
                update_a_book_price_by_name(_name, _price)
    # if you get only price and isbn, not name
    elif _name == "" and _price != "" and _isbn != "":
        if is_book_exists_by_isbn(_isbn):
            update_a_book_price_by_isbn(_isbn, _price)
        pass
    else:
        raise Exception("Insufficient parameters")


# test update_a_book
# update_a_book("The New book","9.99","111112")
# update_a_book("The New book","10.99","")
# update_a_book("","11.99","111112")
# update_a_book("","11.99","")
# print(list_of_books)


# get_a_book(_name, _price, _ISBN): return one book item.
# User input: You may not data for all three parameters always. Deal with what you get.
# Validations: If you have ISBN, return the book with the ISBN.
# Validations: If you have name and price, no ISBN, match for name and price and
#               return a book that matches both name and price, otherwise do not return.
# Validations: If you have only name, return a book that matches name,
#               otherwise (if there are more than one book with same name) do not return.
# Validations: If you have only price, return a book that matches price,
#               otherwise (if there are more than one book with same price) do not return.

def get_a_book(_name, _price, _isbn):
    # if you get isbn, don't need rest
    if _isbn:
        return get_a_book_by_isbn(_isbn)
    elif _name != "" and _price != "":
        if number_of_books_by_name(_name) == 1:
            return get_a_book_by_name_and_price(_name, _price)
        elif number_of_books_by_name(_name) >= 1:
            raise Exception("More than one book with the same name exists")
        else:
            raise Exception("No book with the same name exists")
    elif _name:
        if number_of_books_by_name(_name) == 1:
            return get_a_book_by_name(_name)
        elif number_of_books_by_name(_name) >= 1:
            raise Exception("More than one book with the same name exists")
        else:
            raise Exception("No book with the same name exists")
    elif _price:
        if number_of_books_by_price(_price) == 1:
            return get_a_book_by_price(_price)
        elif number_of_books_by_price(_price) >= 1:
            raise Exception("More than one book with the same price exists")
        else:
            raise Exception("No book with the same price exists")
    else:
        raise Exception("Sorry ...")


# test get_a_book function
# print(get_a_book("", "", "111112"))
# print(get_a_book("The Bible", "", ""))
# print(get_a_book("The Bible", "0.99", ""))
# print(get_a_book("", "1.99", ""))
# print(list_of_books)

# get_all_books(_name, _price, _ISBN): return list of books.
# User input: You may not data for all three parameters always. Deal with what you get.
# Validations: If you have ISBN, return the book with the ISBN.
# Validations: If you have name and price, no ISBN, match for name and price and
#               return a list of books that matches both name and price.
# Validations: If you have only name, return a list of book that matches name.
# Validations: If you have only price, return a list of book that matches price.

def get_all_books(_name, _price, _isbn):
    # if you get isbn, don't need rest
    if _isbn:
        return get_a_book_by_isbn(_isbn)
    elif _name != "" and _price != "":
        if number_of_books_by_name_and_price(_name, _price) >= 1:
            return get_all_books_by_name_and_price(_name, _price)
        else:
            raise Exception("No book with the same name and price exists")
    elif _name:
        if number_of_books_by_name(_name) >= 1:
            return get_all_books_by_name(_name)
        else:
            raise Exception("No book with the same name exists")
    elif _price:
        if number_of_books_by_price(_price) >= 1:
            return get_all_books_by_price(_price)
        else:
            raise Exception("No book with the same price exists")
    else:
        raise Exception("Sorry ...")

# test get_all_books function
# print(get_all_books("The Life and Legacy", "", ""))
# print(get_all_books("", "1.99", ""))
# print(get_all_books("The Life and Legacy", "1.99", ""))
# print(list_of_books)

