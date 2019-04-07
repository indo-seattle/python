print("Exercise B6 - Python functions")

myList = [1, 2, 3, 4, 5]

def sumOfList(list, size):
    if (size != 0):
        return list[size - 1] + sumOfList(list, size - 1)
    else:
        return 0

total = sumOfList(myList, len(myList))

print("Sum of all elements in given list: ", total)