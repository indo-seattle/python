#Write a Python program that takes mylist = ["WA", "CA", "NY", “IL”, “WA”, “CA”, “WA”] and print how many times each state appeared in the list.
mylist = ["WA", "CA", "NY", "IL", "WA", "CA", "WA"]
for x in mylist:
    print(mylist.count(x),x)
print("WA is", mylist.count("WA"), "in the list")
print("CA is", mylist.count("CA"), "in the list")
print("NY is", mylist.count("NY"), "in the list")
print("IL is", mylist.count("IL"), "in the list")