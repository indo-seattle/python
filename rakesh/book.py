"""
Book Module.
Usage :


"""
list_of_books = [{'Name': 'Harry Potter1', 'Price': '10', 'ISBN': '001'},
                 {'Name': 'Harry Potter2', 'Price': '20', 'ISBN': '002'},
                 {'Name': 'Harry Potter3', 'Price': '30', 'ISBN': '003'},
                 {'Name': 'Harry Potter4', 'Price': '40', 'ISBN': '004'},
                 {'Name': 'Harry Potter5', 'Price': '50', 'ISBN': '005'},
                 {'Name': 'Harry Potter6', 'Price': '60', 'ISBN': '006'},
                 {'Name': 'Harry Potter7', 'Price': '70', 'ISBN': '007'},
                 {'Name': 'Harry Potter8', 'Price': '80', 'ISBN': '008'},
                 {'Name': 'Harry Potter9', 'Price': '90', 'ISBN': '009'},
                 {'Name': 'Harry Potter9', 'Price': '100', 'ISBN': '010'},

                 ]


# The break statement, breaks out of the innermost enclosing for or while loop.
# Loop statements may have an else clause; it is executed when the loop terminates through exhaustion of the list (with for) or when the condition becomes false (with while),
# but not when the loop is terminated by a break statement.
def print_items(items):
    """Function call to print list of books.

    Args:
    """
    print('Function call to print list of books.')
    for item in items:
        print(item)


def add_a_book(list_of_books, name, price, isbn):
    print('Function call to add a book.')
    try:
        for each_book in list_of_books:
            if each_book['ISBN'] == isbn:
                raise Exception("The book ", each_book['Name'], "with ISBN number ", each_book['ISBN'],
                                "already exists in the catalog")
                break
        else:
            print("Book doesnt exists")
            list_of_books.append({'Name': name, 'Price': price, 'ISBN': isbn})
    except Exception as err:
        print("An exceptuion occured :", err)


#    return list_of_books


def remove_a_book(list_of_books, isbn):
    print('Function call to remove a book.')
    try:
        for each_book in list_of_books:
            if (isbn in each_book.values()):
                list_of_books.remove(each_book)
                break
        else:
            raise Exception("The book with ISBN number ", isbn, "does not exists in the catalog")
    except Exception as err:
        print("An exceptuion occured :", err)


#    return list_of_books


def update_a_book(name, price, isbn):
    print('Function call to update a book.')
    """Update the book.

    Args :
    Returns :

    """
    try:
        if (name != "" and price != "" and isbn != ""):
            for each_book in list_of_books:
                if (isbn in each_book.values()):
                    each_book["Price"] = price
                    each_book["Name"] = name
        elif (name != "" and price != "" and isbn == ""):
            for each_book in list_of_books:
                if (name in each_book.values()):
                    each_book["Price"] = price
        elif (isbn != "" and price != "" and name == ""):
            for each_book in list_of_books:
                if (isbn in each_book.values()):
                    each_book["Price"] = price
        else:
            print("Two parameters needed to update the book list")

    except Exception as err:
        print("An exceptuion occured :", err)


#    return list_of_books


def get_a_book(name, price, isbn):
    print('Function call to get a book.')
    """Get the book.

    Args :
    Returns :

    """
    try:
        if (name == "" and price == "" and isbn != ""):
            for each_book in list_of_books:
                if (isbn in each_book.values()):
                    print(each_book)
            else:
                print("Book not found in the book list")

        if (name != "" and price != "" and isbn == ""):
            for each_book in list_of_books:
                if (name in each_book.values() and price in each_book.values()):
                    print(each_book)
            else:
                print("Book not found in the book list")

        if (name == "" and price != "" and isbn == ""):
            for each_book in list_of_books:
                if (price in each_book.values()):
                    print(each_book)
            else:
                print("Book not found in the book list")

    except Exception as err:
        print("An exceptuion occured :", err)


#    return list_of_books


def get_all_books(name, price, isbn):
    print('Function call to get a book.')
    """Get the book.

    Args :
    Returns :

    """
    books = []
    try:
        if (name == "" and price == "" and isbn != ""):
            for each_book in list_of_books:
                if (isbn in each_book.values()):
                    books.append(each_book)
            else:
                print("Book not found in the book list")

        if (name != "" and price != "" and isbn == ""):
            for each_book in list_of_books:
                if (name in each_book.values() and price in each_book.values()):
                    books.append(each_book)
            else:
                print("Book not found in the book list")

        if (name != "" and price == "" and isbn == ""):
            for each_book in list_of_books:
                if (name in each_book.values()):
                    books.append(each_book)
            else:
                print("Book not found in the book list")

        if (name == "" and price != "" and isbn == ""):
            for each_book in list_of_books:
                if (price in each_book.values()):
                    books.append(each_book)
            else:
                print("Book not found in the book list")
        print(books)
    except Exception as err:
        print("An exceptuion occured :", err)


#    return list_of_books


def main():
    print("      1: Add Book")
    print("      2: Delete Book")
    print("      3: Update Book")
    print("      4: Display a Book ")
    print("      5: Display all Books")
    print("      6: Exit program")

    menu_choice = input("Enter a selection : ")

    if menu_choice == '1':
        book_name = input("Enter the book name : ")
        book_price = input("Enter the book price : ")
        book_isbn = input("Enter the book isbn : ")
        add_a_book(list_of_books, book_name, book_price, book_isbn)
        print_items(list_of_books)
    elif menu_choice == '2':
        book_name = input("Enter the book name : ")
        book_price = input("Enter the book price : ")
        book_isbn = input("Enter the book isbn : ")
        remove_a_book(list_of_books, book_isbn)
        print_items(list_of_books)
    elif menu_choice == '3':
        book_name = input("Enter the book name : ")
        book_price = input("Enter the book price : ")
        book_isbn = input("Enter the book isbn : ")
        update_a_book(book_name, book_price, book_isbn)
        print_items(list_of_books)
    elif menu_choice == '4':
        book_name = input("Enter the book name : ")
        book_price = input("Enter the book price : ")
        book_isbn = input("Enter the book isbn : ")
        get_a_book(book_name, book_price, book_isbn)
        print_items(list_of_books)
    elif menu_choice == '5':
        book_name = input("Enter the book name : ")
        book_price = input("Enter the book price : ")
        book_isbn = input("Enter the book isbn : ")
        get_all_books(book_name, book_price, book_isbn)
        print_items(list_of_books)
    elif menu_choice == 6:
        print_items(list_of_books)


# get_a_book(list_of_books, name, price, isbn)
# get_all_book(list_of_books, name, price, isbn)

if __name__ == '__main__':
    main()

