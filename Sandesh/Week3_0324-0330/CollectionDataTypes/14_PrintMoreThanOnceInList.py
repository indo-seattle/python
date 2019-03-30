#Write a Python program that takes mylist = [“CAL”, “SEA”, “PIT”, “CAL”] and print the string that appeared more than once.
mylist = ["CAL", "SEA", "PIT", "CAL1"]
mylist.sort()
for x in mylist:
    if x == mylist[1]:
        print(x)
