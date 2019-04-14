"""
Create a set of functions that allow various actitivies on the book:
add_a_book(_name, _price, _ISBN): Add the book to the book list.
Validations: do not add if the book already exists with same ISBN.
Errors: Cannot add this book, a book already exists with the ISBN.
Allow: Multiple books can be with the same name.
remove_a_book(_ISBN): Remove a book from the list.
Errors: Cannot remove this book, no book exists with the ISBN.
update_a_book(_name, _price, _ISBN): Update an existing book.
User input: You may not data for all three parameters always. Deal with what you get.
Validations: If user sends only name and price, update price information for the book with the same name. If you find more than one book with the name, do not update.
Validations: If user sends ISBN, name and price, update name and price information for the book with the ISBN.
Validations: If user sends only ISBN and price, update price information for the book with the same ISBN.
Validations: If user sends only name or price, do not update anything. Return Error saying you need at two paramenters input to perform any operation
get_a_book(_name, _price, _ISBN): return one book item.
User input: You may not data for all three parameters always. Deal with what you get.
Validations: If you have ISBN, return the book with the ISBN.
Validations: If you have name and price, no ISBN, match for name and price and return a book that matches both name and price, otherwise do not return.
Validations: If you have only name, return a book that matches name, otherwise (if there are more than one book with same name) do not return.
Validations: If you have only price, return a book that matches price, otherwise (if there are more than one book with same price) do not return.
get_all_books(_name, _price, _ISBN): return list of books.
User input: You may not data for all three parameters always. Deal with what you get.
Validations: If you have ISBN, return the book with the ISBN.
Validations: If you have name and price, no ISBN, match for name and price and return a list of books that matches both name and price.
Validations: If you have only name, return a list of book that matches name.
Validations: If you have only price, return a list of book that matches price.
"""
from BookShopExceptions import BookNotFoundException
from BookShopExceptions import InvalidBookException

""" Module Constructor """
# global book list of books, where in a book is represented by dictionary
# with keys "_isbn", "_name" and "_price"
global _book_list

_book_list = []


def find_books(_isbn, _name, _price):

    filtered_list = []
    # return list of book if found either using ISBN, or Book or Price

    for book in _book_list:
        if _isbn is not None and _isbn!="":
            if book['isbn'] == _isbn:
                filtered_list.append(book)
                # once isbn is found break the loop
                break
        elif _name is not None and _name!="" \
            and  _price is not None and _price!="":

            if book['name'] == _name \
                    and book['price'] == _price:
                filtered_list.append(book)
                # continue the loop for other books with same name and price
        elif _name is not None and _name!="":
            if book['name'] == _name:
                filtered_list.append(book)
        elif _price is not None and _name!="":
            if book['price'] == _price:
                filtered_list.append(book)

    if len(filtered_list) == 0:
        raise BookNotFoundException("No Book Found with (ISBN:{},Name:{},Price:{})".format(_isbn,_name,_price))

    return filtered_list


def add_a_book(_isbn,_name,_price):
    # adds a book with isbn, name and price to the book list
    # raises an exception if _isbn exists already
    # raises an exception if any of these values are empty

    if _isbn is None or _isbn == "" \
        or _name is None or _name == "" \
            or _price is None or _price == "":

        # raise an exception
        raise InvalidBookException("Book Details cannot be null or empty (ISBN:{},Name:{},Price:{}".format(_isbn,_name,_price))

    # check if there exists a book with ISBN
    try:
        filtered_list = find_books(_isbn,_name,_price)
        if len(filtered_list) > 0:
            print ("Book ({},{},{}) already exists".format(_isbn,_name,_price))
    except BookNotFoundException as ex:
        # add the book now
        book = {'isbn':_isbn,'name':_name,'price':_price}
        _book_list.append(book)
    except Exception as ex:
        print("Book ({},{},{}) could not be added".format(_isbn, _name, _price))
        print(ex)
    finally:
        print ("Thank You")


def remove_a_book(_isbn):

    try:
        if _isbn is not None and _isbn != "":
            filtered_list = find_books(_isbn,None,None)
            # Expected to return only one element
            _book_list.remove(filtered_list[0])
        else:
            raise InvalidBookException ("ISBN must be specified")
    except BookNotFoundException as ex:
        print("Cannot remove this book, no book exists with the ISBN.{}".format(_isbn))
    except InvalidBookException as ex:
        print("You must specify an ISBN value to remove a book from list")


def update_a_book(_isbn,_name,_price):

    try:
        if _isbn is not None and _isbn != "":
            filtered_list = find_books(_isbn,None,None)
            # Expected to return only one element
            if _name is not None and _name != "":
                filtered_list[0]['name'] = _name
            if _price is not None and _name != "":
             filtered_list[0]['price'] = _price
        elif _name is not None and _name != "" \
             and _price is not None and _price != "":

            filtered_list = find_books(None,_name,None)
            if len(filtered_list) > 1:
                raise InvalidBookException("Multiple Books were found with same name ({})".format(_name))
            filtered_list[0]['price'] = _price
        else:
            raise InvalidBookException("Updating a Book requires two parameters (ISBN or Name) and Price")

    except BookNotFoundException as ex:
        print(ex)
    except InvalidBookException as ex:
        print(ex)


# adds the first book into empty book list
print("1. Adds the first book into empty Book List")
add_a_book('111','My Book 1','0.99')
# Attempts to add a 2nd book with same ISBN and fails
print("2. Attempts to add a 2nd Book with same ISBN and fails")
add_a_book('111','My Book 2','1.99')
print("3. Adds a 2nd book with different ISBN with same as firs book")
# adds a 2nd book with different ISBN with same as first book
add_a_book('112','My Book 1','0.99')

print(_book_list)
print("4. Removes the first book")
# removes the first book
remove_a_book('111')
print(_book_list)
# Attempts to remove the same book again and fails
print("5. Attempts to remove the same book again and fails")
remove_a_book('111')
# removes the second book as well
print("6. Removes the 2nd book")
remove_a_book('112')
# empty list
print(_book_list)

# attempts to update the empty list and fails
print("7.Attempts to update an empty list and fails")
update_a_book('111','My Book 1','0.99')
# adds both books again.

add_a_book('111','My Book 1','0.99')
add_a_book('111','My Book 2','1.99')
add_a_book('112','My Book 1','0.99')
add_a_book('113','My Book 2','1.99')
print (_book_list)
# updates the first book price with 1.99
print("8.updates the first book with price 1.99 from 0.99")
update_a_book('111','My Book 1','1.99')
print (_book_list)
# updates the second book by name with price '2.99'
print("9. Updates the 2nd book price by just name to price 2.99")
update_a_book(None,'My Book 2','2.99')
print (_book_list)
print("10. Updates the two books with same name to prices 3.99")
update_a_book(None,"My Book 1","3.99")
print(_book_list)
# Attempts to update by sending only name
update_a_book(None,'My Book 1',None)
update_a_book(None,None,'1.99')

print (_book_list)
