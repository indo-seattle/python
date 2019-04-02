print("Exercise 34 - Collection Data Types")
print("Python way to combine two lists in an alternating fashion")


list1 = ["WA", "CA"]
list2 = ["Washington", "California"]

list3 = []
while True:
    try:
        list3.append(list1.pop(0))
        list3.append(list2.pop(0))
    except IndexError:
        break
print(list3)