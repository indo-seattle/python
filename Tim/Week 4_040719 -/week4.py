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
