#Write a Python program that takes mylist = ["WA", "CA", "NY", “IL”, “WA”, “CA”, “WA”] and print how many times WA appeared in the list.
mylist = ["WA", "CA", "NY", "IL", "WA", "CA", "WA"]
find = input("Enter the state for which you want the count : ")
y = mylist.count(find)
print(y)
