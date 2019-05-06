list_of_books = []

# Continue operation
can_continue = True


# Selection screen
def sel_screen():
    print("Enter 1: Add books")
    print("      2: Delete Books")
    print("      3: Update a Book")
    print("      4: Display a Book details")
    print("      5: Display all Books")


# Display selection options for initial user operation
sel_screen()

# User Input
user_choice = int(input('Enter you choice:'))


# Validate entry

# Add book definition
def add_a_book(name, price, ISBN):
    list_of_books.append({'name': name, 'price': price, 'ISBN': ISBN})

# Delete book definition
def delete_a_book(ISBN):
    for each_book in list_of_books:
        if ISBN in each_book.values():
            if each_book in list_of_books:
                list_of_books.remove(each_book)


# Update book definition
def update_a_book(name, price, ISBN):
    for each_book in list_of_books:
        if ISBN in each_book.values():
            if each_book in list_of_books:
                list_of_books.remove(each_book)


# Get a book definition
def get_a_book(name, price, ISBN):
    for each_book in list_of_books:
        if ISBN in each_book.values():
            if each_book in list_of_books:
                list_of_books.remove(each_book)


# Get all books definition
def get_all_books(name, price, ISBN):
    for each_book in list_of_books:
        if ISBN in each_book.values():
            if each_book in list_of_books:
                list_of_books.remove(each_book)


while can_continue:
    # Enter selection screen values
    book_name = input("Enter Book Name: ")
    book_price = input("Enter price: ")
    book_isbn = input("Enter ISBN: ")

    # Add book
    if user_choice == 1:
        add_a_book(book_name, book_price, book_isbn)
        quest_continue = input("Do you want to continue (Y/N): ")
        if quest_continue == 'N':
            can_continue = False
            # print(list_of_books)
            print('List of books are:', list_of_books)
        elif quest_continue == 'Y':
            can_continue = True
        else:
            quest_continue = input("Please only enter (Y/N): ")
            if quest_continue == 'N':
                can_continue = False
                print('List of books are:', list_of_books)
            elif quest_continue == 'Y':
                can_continue = True


    # Delete book
    elif user_choice == 2:
        delete_a_book('1')
    # Update Book
    elif user_choice == 3:
        delete_a_book('1')
    # Display a book
    elif user_choice == 4:
        delete_a_book('1')
    # Display all books
    elif user_choice == 5:
        print(list_of_books)

