print("Exercise 30 - Collection Data Types")
print("Python print the string that appeared more than once.")


myList = ["CAL", "SEA", "PIT", "CAL"]

myNewList = []

for x in myList:

    if myList.count(x) > 1:
        print(x)
        myNewList.append(x)
print(myNewList)


