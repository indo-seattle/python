#Write a Python program that takes mylist = ["WA", "CA", "NY", “IL”] and print it respective state names (Ex: WA is Washington] for each item in the list.
mylist = ["WA", "CA", "NY", "IL"]
for x in mylist:
    if x == "WA":
        print(x, "is for Washington")
    elif x == "CA":
        print(x, "is for California")
    elif x == "NY":
        print(x, "is for New York")
    elif x == "IL":
        print(x, "is for Illinois")
