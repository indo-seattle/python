print("Exercise 31 - Collection Data Types")
print("Python remove duplicates from the list.")
print("Create a dictionary, using the List items as keys. This will automatically remove any duplicates because dictionaries cannot have duplicate keys.")


myList = ["CAL", "SEA", "PIT", "CAL"]
myList = list(dict.fromkeys(myList))


print(myList)


