print("Exercise 32 - Collection Data Types")
print("Remove all even items in the list")

myList = ["CAL", "SEA", "PIT", "CAL", "POR", "KEN", "NJC"]

i=0
for element in myList:
    if i % 2 != 0:
        pass
    else:
        myList.remove(element)
    i = i + 1

print(myList)


