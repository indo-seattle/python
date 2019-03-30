#Write a Python program that takes mylist = [1, 2, 3, 4, 5] and print middle number from the list.
mylist = [1, 2, 3, 4, 5]
length = len(mylist)
if length%2 != 0:
    print("The middle number is", mylist[int(length/2)])
else:
    print("There is no middle number of even numbers in the list")