#Write a Python program that takes mylist = ["WA", "CA", "NY", “IL”, “WA”, “CA”, “WA”] and print how many times WA appeared in the list.

mylist = ["WA", "CA", "NY", "IL", "WA", "CA", "WA"]
count = 0
print("Available list is:", mylist)
print("Enter the State")
userinput = input()
for i in mylist:
    if i == userinput:
        count += 1;
print( userinput, "has appeared", count, "times in the list")