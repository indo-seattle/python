print("Exercise 35 - Collection Data Types")
print("Python way to sort the list ascending without using sort function.")


myList = [6, 2, 7, 3, 4, 5]
myNewList = []

while myList:
    minimum = myList[0]
    for element in myList:
        if element < minimum:
            minimum = element
    myNewList.append(minimum)
    myList.remove(minimum)

print(myNewList)