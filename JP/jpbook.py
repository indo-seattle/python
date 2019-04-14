# Exercise:
# Create a module called Book.py
# Create a variable: book list
## book = [{ ‘name’: ‘test’, ‘price’: ‘0.99’, ‘ISBN’: ‘111’},
#  { ‘name’: ‘test1’, ‘price’: ‘1.99’, ‘ISBN’: ‘112’}]
# Coding standards:
# Create a descriptive variables. All small caps, words separated by _
# Create a set of functions that allow various actitivies on the book:


# Additional homework:
# Practice using all built-in functions of list and dictionary. Create your own help document that you can refer to.




from pprint import pprint as pp


list_of_books = [{'name': 'bible1', 'price':'1.99','ISBN':'1111'},
                 {'name': 'bible2', 'price':'2.99','ISBN':'2222'}]
print("Initial list of books :\n")
pp(list_of_books)



def go_to_menu():
    flag = True
    ch = input('\nDo you want to go to Main menu (Y/N)? ')
    if ch.capitalize() != "Y":
        flag = False
    return flag

# add_a_book(_name, _price, _ISBN): Add the book to the book list.
# Validations: do not add if the book already exists with same ISBN.
# Errors: Cannot add this book, a book already exists with the ISBN.
# Allow: Multiple books can be with the same name.

def add_a_book(name,price,ISBN):
    try:
        isbn_values =[]
        for book in list_of_books:
            isbn_values.append(book.get('ISBN'))
            # print(isbn_values)
        if ISBN in isbn_values:
            raise Exception ("Cannot add this book, a book already exists with the ISBN")
        else:
            list_of_books.append({'name': name, 'price': price, 'ISBN': ISBN})
    except Exception as err:
        print(err)
    return list_of_books

# remove_a_book(_ISBN): Remove a book from the list.
# Errors: Cannot remove this book, no book exists with the ISBN.

def remove_a_book(ISBN):
    try:
        book = [item for item in list_of_books if item['ISBN'] == ISBN]
        if len(book) != 0:
            print("Removing item", book)
            list_of_books.remove(book[0])
        else:
            raise Exception("\nCannot delete this book, no book exists with given ISBN\n")
    except Exception as err:
        print(err)

# update_a_book(_name, _price, _ISBN): Update an existing book.
# User input: You may not data for all three parameters always. Deal with what you get.
# Validations: If user sends only name and price, update price information for the book with the same name. If you find more than one book with the name, do not update.
# (done) Validations: If user sends ISBN, name and price, update name and price information for the book with the ISBN.
# (done) Validations: If user sends only ISBN and price, update price information for the book with the same ISBN.
# Validations: If user sends only name or price, do not update anything. Return Error saying you need at two paramenters input to perform any operation

def update_a_book(name, price,ISBN):
    try:
        print("\nname :{}, price : {}, ISBN :{} ".format(name,price,ISBN))
        if ISBN != '0000':                                   ## Loop that has valid ISBN provided
            update_book = [item for item in list_of_books if item['ISBN'] == ISBN]
            print("Update_book", update_book)
            if len(update_book) > 1:
                raise Exception(" Multiple books exist with same ISBN")
            elif len(update_book) == 1:
                if name == 'dummy' and price != '0.00':     ### ISBN, price given
                    update_book[0]['price'] = price
                elif name != 'dummy' and price == '0.00':   ### ISBN, Name given
                    update_book[0]['name'] = name
                else:                                       ### ISBN, Name and price given
                    update_book[0]['name'] = name
                    update_book[0]['price'] = price
            else:
                raise Exception ("No book exists with given information")
        elif name != 'dummy' and price != '0.00':
            update_book = [item for item in list_of_books if item['name'] == name]
            print("Update_book", update_book)
            if len(update_book) > 1:
                raise Exception (" Multiple names exist with same name")
            elif len(update_book) == 1:
                update_book[0]['price'] = price
            else:
                raise Exception ("No book exists with given name and price!")
        else:
            raise Exception ("Insufficient information provided. Need atleast two params for update operation!")
    except Exception as err:
        print(err)
    return list_of_books

# get_a_book(_name, _price, _ISBN): return one book item.
# User input: You may not data for all three parameters always. Deal with what you get.
# Validations: If you have ISBN, return the book with the ISBN.
# Validations: If you have name and price, no ISBN, match for name and price and return a book that matches both name and price, otherwise do not return.
# Validations: If you have only name, return a book that matches name, otherwise (if there are more than one book with same name) do not return.
# Validations: If you have only price, return a book that matches price, otherwise (if there are more than one book with same price) do not return.

def get_a_book(name, price, ISBN):
    book = []
    try:
        print("\nname :{}, price : {}, ISBN :{} ".format(name,price,ISBN))
        if ISBN != '0000':                                   ## Loop that has valid ISBN provided
            got_book = [item for item in list_of_books if item['ISBN'] == ISBN]
            if len(got_book) > 1:
                raise Exception(" Multiple books exist with same ISBN: {}".format(ISBN))
            elif len(got_book) == 1:
                if name == 'dummy' and price != '0.00':     ### ISBN, price given
                    if got_book[0]['price'] == price:
                        book = got_book
                    else:
                        raise Exception ("There is no book matching given info ISBN:{}, price:{}".format(ISBN,price))
                elif name != 'dummy' and price == '0.00':     ### ISBN, name given
                    if got_book[0]['name'] == name:
                        book = got_book
                    else:
                        raise Exception ("There is no book matching given info ISBN:{}, name:{}".format(ISBN,name))
                elif name != 'dummy' and price != '0.00':     ### ISBN, name, price given
                    if got_book[0]['price'] == price and got_book[0]['name'] == name:
                        book = got_book
                    else:
                        raise Exception ("There is no book matching given info ISBN:{}, name:{}, price:{} ".format(ISBN,name,price))
                else:
                    book = got_book
            else:
                raise Exception("No book exists with given Info name:{}, price:{}, ISBN: {}".format(name,price,ISBN))
        elif name != 'dummy':
            got_book = [item for item in list_of_books if item['name'] == name]
            if len(got_book) > 1:
                raise Exception(" Multiple books exist with same name: {}".format(name))
            elif len(got_book) == 1:
                if price != '0.00':        ### Name, price given
                    if got_book[0]['price'] == price:
                        book = got_book
                    else:
                        raise Exception("There is no book matching given info name:{}, price:{}".format(name, price))
                else:                       #### Only name given
                    book = got_book
            else:
                raise Exception("No book exists with given Info name:{}, price:{}, ISBN: {}".format(name, price, ISBN))
        elif price != '0.00':
            got_book = [item for item in list_of_books if item['price'] == price]
            if len(got_book) > 1:
                    raise Exception(" Multiple books exist with same price: {}".format(price))
            elif len(got_book) == 1:
                book = got_book
        else:
            raise Exception("There is no book matching given info name:{}, price:{}, ISBN:{}".format(name, price, ISBN))
    except Exception as err:
        print(err)
    return book




# get_all_books(_name, _price, _ISBN): return list of books.
# User input: You may not data for all three parameters always. Deal with what you get.
# Validations: If you have ISBN, return the book with the ISBN.
# Validations: If you have name and price, no ISBN, match for name and price and return a list of books that matches both name and price.
# Validations: If you have only name, return a list of book that matches name.
# Validations: If you have only price, return a list of book that matches price.


def get_all_books(name, price, ISBN):
    books = []
    try:
        print("\nname :{}, price : {}, ISBN :{} ".format(name,price,ISBN))
        if ISBN != '0000':  ## Loop that has valid ISBN provided
            got_books = [item for item in list_of_books if item['ISBN'] == ISBN]
            if len(got_books) >= 1:
                if name == 'dummy' and price != '0.00':  ### ISBN, price given
                    got_books_combo = [item for item in list_of_books if item['ISBN'] == ISBN and item['price'] == price]
                    if len(got_books_combo) > 0:
                        books = got_books_combo
                    else:
                        raise Exception ("There is no book matching given info")
                elif name != 'dummy' and price == '0.00':  ### ISBN, name given
                    got_books_combo = [item for item in list_of_books if item['ISBN'] == ISBN and item['name'] == name]
                    if len(got_books_combo) > 0:
                        books = got_books_combo
                    else:
                        raise Exception("There is no book matching given info")
                elif name != 'dummy' and price != '0.00':  ### ISBN, name, price given
                    got_books_combo = [item for item in list_of_books if item['ISBN'] == ISBN and item['name'] == name and item['price'] == price]
                    if len(got_books_combo) > 0:
                        books = got_books_combo
                else:
                    books = got_books
            else:
                raise Exception("No book exists with given Info name:{}, price:{}, ISBN: {}".format(name, price, ISBN))

        elif name != 'dummy':
            got_books = [item for item in list_of_books if item['name'] == name]
            if len(got_books) >= 1:
                if price != '0.00':  ### Name, price given
                    got_books_combo = [item for item in list_of_books if item['price'] == price and item['name'] == name]
                    if len(got_books_combo) > 0:
                        books = got_books_combo
                    else:
                        raise Exception("There is no book matching given info")
                else:  #### Only name given
                    books = got_books
            else:
                raise Exception("There is no book matching given info name:{}, price:{}".format(name, price))
        elif price != '0.00':
            got_books = [item for item in list_of_books if item['price'] == price]
            if len(got_books) >= 1:
                books = got_books
            else:
                raise Exception("There is no book matching given info name:{}, price:{}, ISBN:{}".format(name, price, ISBN))
    except Exception as err:
        print(err)
    return books







################## Main loop ######################


while go_to_menu():
    print('\n########## Main Menu ###########')
    print('1) Add Book(s)')
    print('2) Delete book')
    print('3) Update a book')
    print('4) Get a book')
    print('5) Get all books')
    print('Q) Quit the program')
    print('########################################')
    print('\nCurrent list of books : ')
    pp(list_of_books)
    menu_choice = input("\n\nPlease select a number (1 - 5) or Q to quit: ")
    if menu_choice == '1':
        # Add book to list_of_books
        num_of_books = int(input("How many number of books you would like to add ?"))
        print(num_of_books)
        for each_book in range(num_of_books):
            bk_name = input("Enter book name : ")
            bk_price = input("Enter Price of the book : ")
            bk_isbn = input("Enter ISBN code of the book : ")
            add_a_book(bk_name, bk_price, bk_isbn)
        print("List of books after addition :")
        pp(list_of_books)
    elif menu_choice == '2':
        # Delete book from list_of_books
        bk_isbn = input("Enter ISBN code of the book to be deletes : ")
        remove_a_book(bk_isbn)
        print("List of books after deleting :")
        pp(list_of_books)
    elif menu_choice == '3':
        # update book with various data input from user
        bk_name = input("Enter book name or press enter for default value (dummy) :")
        if bk_name == '':
            bk_name = 'dummy'
        print(bk_name)
        bk_price = input("Enter Price of the book or press enter for default value($0.00) : ")
        if bk_price == '':
            bk_price = '0.00'
        bk_isbn = input("Enter ISBN code of the book or press enter for default value (0000): ")
        if bk_isbn == '':
            bk_isbn = '0000'
        update_a_book(bk_name,bk_price,bk_isbn)
        print("List of books after updating :")
        pp(list_of_books)
    elif menu_choice == '4':
        bk_name = input("Enter book name or press enter if you do not want to enter :")
        if bk_name == '':
            bk_name = 'dummy'
        bk_price = input("Enter Price of the book or press enter if you do not want to enter : ")
        if bk_price == '':
            bk_price = '0.00'
        bk_isbn = input("Enter ISBN code of the book or press enter if you do not want to enter: ")
        if bk_isbn == '':
            bk_isbn = '0000'
        result = get_a_book(name=bk_name, price=bk_price, ISBN=bk_isbn)
        print("\nHere is the book found matching reqs")
        pp(result)
    elif menu_choice == '5':
        bk_name = input("Enter book name or press enter if you do not want to enter :")
        if bk_name == '':
            bk_name = 'dummy'
        bk_price = input("Enter Price of the book or press enter if you do not want to enter : ")
        if bk_price == '':
            bk_price = '0.00'
        bk_isbn = input("Enter ISBN code of the book or press enter if you do not want to enter: ")
        if bk_isbn == '':
            bk_isbn = '0000'
        result = get_all_books(name=bk_name, price=bk_price, ISBN=bk_isbn)
        print("\nHere is the list of books found matching reqs")
        pp(result)
    elif menu_choice.capitalize() == "Q":
        print('Bye, See you later!')
        break
    else:
        c = input('OOPS! Invalid Input!! Do you want to try again? (Y/N) :')
        if c.capitalize() == "Y":
            continue
        else: break

