#Write a Python program that takes mylist = ["WA", "CA", "NY", “IL”] and print it respective state names (Ex: WA is Washington] for each item in the list.

mylist = ["WA", "CA", "NY", "IL"]
for i in mylist:
    if i == "WA":
        print(i, "is Washington")
    elif i == "CA":
        print(i, "is California")
    elif i == "NY":
        print(i, "is NewYork")
    else:
        print(i, "is Illinois")