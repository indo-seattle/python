#! /usr/bin/env python3
""" Book Module...
    This contains all the book related functions.
    Author: ISCF Development Team 2
    Functions:

    """

list_of_books = [
    {'name': 'Intro to Python',
     'price': 9.99,
     'isbn': 'PY123'
     },
    {'name': 'Intro to ML',
     'price': 19.99,
     'isbn': 'ML123'
     },
    {'name': 'Intro to AI',
     'price': 9.99,
     'isbn': 'AI123'
     },
    {'name': 'Intro to Java',
     'price': 29.99,
     'isbn': 'JAVA123'
     },
    {'name': 'Intro to Java',
     'price': 29.99,
     'isbn': 'JAVA124'
     }
]


# print(list_of_books)


def get_all_books():
    """ Prints all the books available in the Book Database
    Parameters: No Parameters..."""
    print('Getting all books from Book Database.....')
    for books in list_of_books:
        # print(books)
        print()
        print(f'S.No# {list_of_books.index(books) + 1}')
        for name, book in books.items():
            print(f'{name.capitalize().ljust(5)} : {book} ')


def search_books(book_name, book_price, book_isbn):
    """ Returns  books for a given name and ISBN or Price
       Arguments: Book_name
                  Book_price
                  Book_Isbn

       Returns:   Books that matches with the given criteria"""
    book_data = []
    results = ''
    for book in list_of_books:
        if book_isbn.strip() != '':
            if book_isbn in book.values():
                book_data.append(f'Book Name : {book["name"].ljust(11)}\nPrice     : {str(book["price"]).ljust(11)}\nISBN      : {book["isbn"].ljust(11)} ')

        elif book_name.strip() != '' and book_price.strip() != '':
            if book_name in book.values() and float(book_price) == book['price']:
                book_data.append(f'Book Name : {book["name"].ljust(11)}\nPrice     : {str(book["price"]).ljust(11)}\nISBN      : {book["isbn"].ljust(11)} ')
        elif book_name.strip() != '':
            if book_name in book.values():
                book_data.append(f'Book Name : {book["name"].ljust(11)}\nPrice     : {str(book["price"]).ljust(11)}\nISBN      : {book["isbn"].ljust(11)} ')
        elif book_price.strip() != '':
            if float(book_price) in book.values():
                book_data.append(f'Book Name : {book["name"].ljust(11)}\nPrice     : {str(book["price"]).ljust(11)}\nISBN      : {book["isbn"].ljust(11)} ')


    #    return 'No Books found for the given search criteria'
    #elif book_counter == 1:
    if len(book_data) == 0:
        results = 'No Books found with given Criteria'
    for r in book_data:
        results += r + '\n'
    return results
    #else:
     #   return 'Multiple books found with the given criteria.'


def search_books_wrapper():
    print('Enter Book Name')
    name = input()
    print('Enter Book Price')
    price = input()
    print('Enter Book ISBN')
    isbn = input()
    data = search_books(name, price, isbn)
    print(data)


def get_a_book_wrapper():
    print('Enter Book Name')
    name = input()
    print('Enter Book Price')
    price = input()
    print('Enter Book ISBN')
    isbn = input()
    print(f'Calling get a book api -- {name} {price} {isbn}')
    data = get_a_book(name, price, isbn)
    print(data)


def update_a_book_wrapper():
    print('Enter Book Name')
    name = input()
    print('Enter Book Price')
    price = input()
    print('Enter Book ISBN')
    isbn = input()
    print(f'Calling update a book api -- {name} {price} {isbn}')
    status = update_a_book(name, price, isbn)
    print(status)


def update_a_book(book_name, book_price, book_isbn):
    """ Updates a book and Returns status for a given name and ISBN or Price
       Arguments: Book_name
                  Book_price
                  Book_Isbn

       Returns:   Status of the Update request """
    book_counter = 0
    book_data = {}
    status = ''
    for book in list_of_books:
        if book_isbn.strip() != '':
            if book_isbn in book.values():
                book_counter += 1
                book_data = book
                if book_name.strip() != '':
                    book_data['name'] = book_name
                if book_price.strip() != '':
                    book_data['price'] = book_price
                # book.update(book_data)
                status = f'Successfully Updates ISBN {book_isbn}'
            else:
                status = f'No book found with ISBN : {book_isbn}'

        elif book_name.strip() != '' and book_price.strip() != '':
            if book_name in book.values():
                book_counter += 1
                book_data = book
                if book_price.strip() != '':
                    book_data['price'] = book_price

        elif book_name.strip() != '':
            status = 'At least 2 Parameters are needed to update the Book!'
        elif book_price.strip() != '':
            status = 'At least 2 Parameters are needed to update the Book!'

    print(f'Counter {book_counter}')
    if book_counter == 0:
        return status
    elif book_counter == 1:
        for each_book in list_of_books:
            if book_isbn in each_book.values() or book_name in each_book.values():
                each_book.update(book_data)

        return 'Successfully Updated Book'
    else:
        return 'Multiple books found with the given criteria.'


def get_a_book(book_name, book_price, book_isbn):
    """ Returns a book for a given name and ISBN or Price
       Arguments: Book_name
                  Book_price
                  Book_Isbn

       Returns:   Book that matches with the given criteria"""
    book_counter = 0
    book_data = ''
    for book in list_of_books:
        if book_isbn.strip() != '':
            if book_isbn in book.values():
                book_counter += 1
                book_data = f'Book Name : {book["name"].ljust(11)}\nPrice     : {str(book["price"]).ljust(11)}\nISBN      : {book["isbn"].ljust(11)} '
            else:
                book_data = f'No book found with ISBN : {book_isbn}'

        elif book_name.strip() != '' and book_price.strip() != '':
            if book_name in book.values() and float(book_price) == book['price']:
                book_counter += 1
                book_data = f'Book Name : {book["name"].ljust(11)}\nPrice     : {str(book["price"]).ljust(11)}\nISBN      : {book["isbn"].ljust(11)} '
        elif book_name.strip() != '':
            if book_name in book.values():
                book_counter += 1
                book_data = f'Book Name : {book["name"].ljust(11)}\nPrice     : {str(book["price"]).ljust(11)}\nISBN      : {book["isbn"].ljust(11)} '
        elif book_price.strip() != '':
            if float(book_price) in book.values():
                book_counter += 1
                book_data = f'Book Name : {book["name"].ljust(11)}\nPrice     : {str(book["price"]).ljust(11)}\nISBN      : {book["isbn"].ljust(11)} '
    print(f'Counter {book_counter}')
    if book_counter == 0:
        return 'No Books found for the given search criteria'
    elif book_counter == 1:
        return book_data
    else:
        return 'Multiple books found with the given criteria.'


def add_a_book(book_name, book_price, book_isbn):
    """This function is used to add a Book to the Book Database
    Parameters: book_name
                book_price
                book_isbn
    Returns:  None
                """
    print('Adding a book ....')
    if book_name is None or book_name.strip() == '':
        print('Book Name is mandatory!')
        return
    # Check if the ISBN Already exists in the Database..
    for book_list in list_of_books:
        if book_isbn.upper() in book_list.get('isbn').upper():
            print(book_list)
            print(f'Uh..oh!..Looks like there is a book already with ISBN {book_isbn}..this action cannot be done.')
            return
    print('This is a New Book, Adding to the Database')
    add_book = {'name': book_name, 'price': book_price, 'isbn': book_isbn}
    list_of_books.append(add_book)


# add_a_book('Intro to AI', 29.99, 'AI123')
# print(f'After adding book {list_of_books}')


# if 'Intro to Python' in list_of_books:
#     print('Exists')
# else:
#     print('No...')
""" This Functions deletes a book from the Database.
      Parameters: book_isbn"
      Returns: None """


def delete_a_book(book_isbn):
    print('Deleting a book.....')
    status = ''
    for book_list in list_of_books:
        if book_isbn in book_list.values():
            print(f'Book with ISBN {book_isbn} found. Deleting it..')
            list_of_books.remove(book_list)
            status = f'Successfully deleted Book with ISBN {book_isbn}'
        else:
            status = f'No book exists with ISBN {book_isbn}'
    return status


def delete_a_book_wrapper():
    print('Enter Book ISBN to be removed')
    isbn = input()
    status = delete_a_book(isbn)
    print(status)

# delete_a_book('AI123')
# print(list_of_books)


def delete_book_by_name(book_name):
    pass


def delete_book_by_isbn(book_isbn):
    pass


def add_a_book_wrapper():
    print('You are in Add a book Function...Please follow the prompts and enter the requested details')
    add_status = 1
    while add_status:
        print('Enter a Book Name')
        name = input()
        print('Enter Price')
        price = input()
        print('Enter ISBN number')
        isbn = input()
        print(f'The Details given \n Name :{name}  Price : {price} ISBN : {isbn}')
        while True:
            print('Enter "Y" to Add book or "N" to start over again')
            option = input()
            if option.upper() == 'Y':
                add_a_book(name, price, isbn)
                add_status = 0
                break
            elif option.upper() == 'N':
                print('Starting all over again....')
                add_status = 1
                break
            else:
                print('Incorrect Option selected...')


def book_program():
    print('This is the Book Program!')
    print('---------------------------')
    while True:
        print('-------------------------------------------------------------')
        print('Please select the function you want to Perform, Pick a Number')
        print('1. Get all Books')
        print('2. Add a Book')
        print('3. Get a Book')
        print('4. Delete a Book')
        print('5. Update a Book')
        print('6. Search Books')
        print('q to Exit')
        user_input = input()
        if str(user_input).lower() == 'q':
            print('Exiting the Book Program....Hope you liked it!')
            break
        else:
            if user_input.isdigit():
                print(f'The Function No#  {int(user_input)}')
                func_option = int(user_input)
                if func_option == 1:
                    get_all_books()
                elif func_option == 2:
                    add_a_book_wrapper()
                elif func_option == 3:
                    get_a_book_wrapper()
                elif func_option == 4:
                    delete_a_book_wrapper()
                elif func_option == 5:
                    update_a_book_wrapper()
                elif func_option == 6:
                    search_books_wrapper()
            else:
                print(f'Invalid Input "{user_input}", Please enter the number from the below list ')

            pass


if __name__ == '__main__':
    book_program()
