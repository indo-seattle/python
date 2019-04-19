#!/usr/sbin/env python3

"""gets all books, gets a books, adds a books, updates a books

usage:

    python3 Book.py <name> <price> <ISBN>
"""
import sys

book = [{ "name": "test", "price": "0.99", "ISBN": "111"},
          { "name": "test1", "price": "1.99", "ISBN": "112"}]


def add_a_book(_name, _price, _ISBN):
    """ Add a books to the list of books

        Args:
            name - the title of the books
            price - the price of the books
            ISBN - the ISBN code of the books
    """
    try:
        book_dict = {}
        book_dict["name"] = _name
        book_dict["price"] = _price
        book_dict["ISBN"] = _ISBN

        # validation - do not add if the books already exists with the same ISBN
        book_exists = False
        for b in range(len(book)):
            if (book[b]["ISBN"] == _ISBN):
                book_exists = True
                break
        # Validations: do not add if the books already exists with same ISBN.
        # Errors: Cannot add this books, a books already exists with the ISBN.
        if (book_exists):
            print("Error: Cannot add this books, a books already exists with the ISBN.::" + str(_ISBN))
        else:
            book.append(book_dict)
            print(" Added the books with ISBN.::" + str(_ISBN))

    except BaseException as e:
        print("Exception raised in adding a books" + str(e) )



def remove_a_book(_ISBN):
    """ remove a books with a given ISBN

        Args:
            ISBN of the books to be removed
    """
    try:
        for b in range(len(book)):
            if ( book[b]["ISBN"] == _ISBN ) :
                book.remove(b)
                print("removed books with ISBN :::" + str(_ISBN))
                break
            else:
                # Errors: Cannot remove this books, no books exists with the ISBN.
                print ( "Error: Cannot remove this books, no books exists with the ISBN.")
    except BaseException as e:
        print("Exception raised in removing a books" + str(e))



def get_a_book(_name, _price, _ISBN):
    """ Search for a books

        Args:
            name - the title of the books
            price - the price of the books
            ISBN - the ISBN code of the books

        Returns:
            returns the books that matches the name, price and ISBN
    """
    try:
        match_by_name_flag = False
        match_by_price_flag = False
        matched_book_by_name = {}
        matched_book_by_price = {}
        for b in range(len(book)):
            a_book = book[b]
            print(a_book)

            # Validations: If you have ISBN, return the books with the ISBN.
            if ( a_book.get("ISBN") == _ISBN ):
                return a_book
            # Validations: If you have name and price, no ISBN, match for name and price and return a books that matches both name and price, otherwise do not return.
            elif ( a_book.get("name")==_name and a_book.get("price")==_price):
                return a_book
            # Validations: If you have only name, return a books that matches name, otherwise (if there are more than one books with same name) do not return.
            elif ( a_book.get("name")==_name ):
                if (match_by_name_flag):
                    print (" Multiple matches with the same name:: " + _name )
                    break
                match_by_name_flag = True
                matched_book_by_name = a_book
            # Validations: If you have only price, return a books that matches price, otherwise (if there are more than one books with same price) do not return.
            elif (a_book.get("price") == _price):
                if (match_by_price_flag):
                    print(" Multiple matches with the same price:: " + _price)
                    break
                match_by_price_flag = True
                matched_book_by_price = a_book
        if (match_by_name_flag):
            return matched_book_by_name
        if (match_by_price_flag):
                return matched_book_by_price
    except BaseException as e:
        print("Exception raised in getting a books" + str(e))


def update_a_book(_name, _price, _ISBN):
    """ update the details of the books

        Args:
            name - the title of the books
            price - the price of the books
            ISBN - the ISBN code of the books

    """
    try:
        matched_by_name_flag = False
        matched_book_by_name = {}
        matched_by_isbn_flag = False
        matched_book_by_isbn = {}

        for b in range(len(book)):
            a_book = book[b]
            print(a_book)

            # Validations: If user sends only name and price,
            #               update price information for the books with the same name.
            #               If you find more than one books with the name, do not update.
            if (a_book.get("name") == _name and _price ):
                if (matched_by_name_flag):
                    print (" Multiple matches with the same name:: " + _name )
                    break
                matched_by_name_flag = True
                matched_book_by_name = a_book
                print("found a matched books by name : " +  _name )
                continue

            # Validations: If user sends ISBN, name and price,
            #               update name and price information for the books with the ISBN.
            if (a_book.get("ISBN") == _ISBN and _name and _price):
                if (matched_by_isbn_flag):
                    print (" Multiple matches with the same ISBN:: " + _ISBN )
                    break
                matched_by_isbn_flag = True
                matched_book_by_isbn = a_book
                print("found a matched books by ISBN : " + _ISBN)
                continue



        # Validations: If user sends only ISBN and price, update price information for the books with the same ISBN.
            if (a_book.get("ISBN") == _ISBN and _price ):
                if (matched_by_isbn_flag):
                    print (" Multiple matches with the same ISBN:: " + _ISBN )
                    break
                matched_by_isbn_flag = True
                matched_book_by_isbn = a_book
                print("found a matched books by ISBN : " +  _ISBN )
                continue


        # Validations: If user sends only name or price, do not update anything.
        #               Return Error saying you need at two paramenters input to perform any operation
            if ( (_name and not _price and not _ISBN ) or (_price and not _name and not _ISBN )):
                print("Error : Need atleast two paramenters as input to perform any operation")


        if ( matched_by_name_flag and _name and _price ):
            matched_book_by_name["price"] = _price
            return matched_book_by_name
        elif ( not matched_by_name_flag and _name and _price ):
            print ( " No books matched by that name : " + _name )
        elif (matched_by_isbn_flag and _ISBN and _name and _price):
            matched_book_by_isbn["price"] = _price
            matched_book_by_isbn["name"] = _name
            return matched_book_by_isbn
        elif (not matched_by_isbn_flag and _ISBN and _name and _price):
            print(" No books matched by that ISBN : " + _ISBN)
        elif ( matched_by_isbn_flag and _price ):
            matched_book_by_isbn["price"] = _price
            return matched_book_by_isbn
        elif ( not matched_by_isbn_flag and _price ):
            print ( " No books matched by that ISBN : " + _ISBN )

    except BaseException as e:
        print("Exception raised in updating a books" + str(e))



def get_all_books(_name, _price, _ISBN):
    """ Get all the books matching the criteria

        Args:
            name - the title of the books
            price - the price of the books
            ISBN - the ISBN code of the books

    """
    try:
        matched_book_list = []
        a_book = {}
        for b in range(len(book)):
            a_book = book[b]
            print( a_book )
            # Validations: If you have ISBN, return the books with the ISBN.
            if ( a_book.get("ISBN") == _ISBN ):
                return a_book
            # Validations: If you have name and price, no ISBN, match for name and price and return a list of books that matches both name and price.
            elif ( a_book.get("name")==_name and a_book.get("price")==_price):
                matched_book_list.append(a_book)
                continue
            # Validations: If you have only name, return a list of books that matches name.
            elif ( a_book.get("name")==_name ):
                matched_book_list.append(a_book)
                continue
            # Validations: If you have only price, return a list of books that matches price.
            elif ( a_book.get("price")==_price ):
                matched_book_list.append(a_book)
                continue

        return matched_book_list

    except BaseException as e:
        print("Exception raised in getting all books" + str(e))


def main(_name, _price, _ISBN):
    """ Main method that call all the methods to Get all the books, get a books, update a books and add a books

        Args:
            name - the title of the books
            price - the price of the books
            ISBN - the ISBN code of the books

    """
    get_all_books(_name, _price, _ISBN)
    get_a_book(_name, _price, _ISBN)
    update_a_book(_name, _price, _ISBN)
    add_a_book(_name, _price, _ISBN)

if __name__ == '__main__':
    main(sys.argv[1],sys.argv[2],sys.argv[3])
