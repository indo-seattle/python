# This module is for book shop app

# Create a list for books which has dictionaries in it, each book is stored as a dictionary
list_of_books = [{'name': 'book1', 'price': '1', 'isbn': '111'},
                 {'name': 'book2', 'price': '1.2', 'isbn': '112'},
                 {'name': 'book2', 'price': '1.2', 'isbn': '113'}
                 ]
# raise valuerror
# function for adding the new book with unique isbn
def add_a_book(name, price, isbn):
    # Getting the list of all ISBNs as I was not able to get the append working for FOR loop
    all_isbn = [each_book['isbn'] for each_book in list_of_books]
    if (isbn in all_isbn):
        print("A book with same ISBN is already present, please try a different ISBN")
    else:
        list_of_books.append({'name': name, 'price': price, 'isbn': isbn})
        print(list_of_books)

# function for deleting a book using isbn
def remove_a_book(isbn):
    all_isbn = [each_book['isbn'] for each_book in list_of_books]
    if (isbn in all_isbn):
        for each_book in list_of_books:
            if (isbn in each_book.values()):
                list_of_books.remove(each_book)
                print ("Removed the book", each_book)
    else:
        print("Book not found, please try a different ISBN")
        print(list_of_books)

# function to update a book with at least two parameters passed
#update_a_book(_name, _price, _ISBN): Update an existing book.
#User input: You may not data for all three parameters always. Deal with what you get.
#Validations: If user sends ISBN, name and price, update name and price information for the book with the ISBN.
#Validations: If user sends only ISBN and price, update price information for the book with the same ISBN.
#Validations: If user sends only name or price, do not update anything. Return Error saying you need at two paramenters input to perform any operation
#Validations: If user sends only name and price, update price information for the book with the same name. If you find more than one book with the name, do not update.
from builtins import Exception

list_of_books = [{ 'name': 'test0', 'price': '0.99', 'ISBN': '111'},
                 { 'name': 'test1', 'price': '1.99', 'ISBN': '112'},
                 { 'name': 'test1', 'price': '1.99', 'ISBN': '113'}
                 ]

def update_a_book(_name, _price, _isbn):
    for each_book in list_of_books:
        ##Validations: If user sends ISBN, name and price, update name and price information for the book with the ISBN.
        if (_isbn in each_book.values() and (_name != None) and (_price != None) and (_isbn != none)):
            each_book.update({'name': _name, 'price': _price, 'ISBN' : _isbn})
            print ("I've updated the book successfully")
        ##Validations: If user sends only ISBN and price, update price information for the book with the same ISBN.
        if(_isbn in each_book.values() and (_name is None) and (_price != None) and (_isbn != None)):
            each_book.update({'name': each_book['name'], 'price' : _price , 'ISBN' : _isbn })
            print ("I've updated the book successfully elif")
        ##Validations: If user sends only name or price, do not update anything. Return Error saying you need at two paramenters input to perform any operation
        if((_isbn is None) and ((_name is None) and (_price != None))):
            raise Exception("You need at least two paramenters input to perform any operation not only PRICE")
        if ((_isbn is None) and ((_name != None) and (_price is None))):
            raise Exception("You need at least two paramenters input to perform any operation no only NAME")
        # All None
        if ((_isbn is None) and ((_name is None) and (_price is None))):
            raise Exception("Please enter at least two parameters to perform any operations")
        ##Validations: If user sends only name and price, update price information for the book with the same name.
        # If you find more than one book with the name, do not update.
        if ((_isbn is None) and (_name != None) and (_price != None)):
            if((each_book['name']) == _name):
                #print(count)
                count = 0
                for each_book['name'] in each_book:
                    count = count + 1
                    #print("sec", count)
                    if (count >1):
                        raise Exception("Name is duplicate")
                        continue
                    else:
                        print(each_book)
                        each_book.update({'name': _name, 'price' : _price , 'ISBN' : each_book['ISBN']})


update_a_book('test0','10', None)
print (list_of_books)


#remove_a_book('11')
#add_a_book( name='book1', price= '1', isbn= '11')
#add_a_book('book1', '1', '11')
#update_a_book( name= '1', price = 'book1', isbn = None)
#update_a_book()
print(list_of_books)