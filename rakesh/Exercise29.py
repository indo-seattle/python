print("Exercise 29 - Collection Data Types")
print("Python: print middle number from the list.")

myList = [1, 2, 3, 4, 5]
middle = float(len(myList)) / 2
if middle % 2 != 0:
    x = myList[int(middle - .5)]
else:
    x = (myList[int(middle)], myList[int(middle - 1)])

print(x)







