"""
String problems
"""
#1.	Write Python program to print “Washington”, then find out it’s length and print it.
# print("Given string is: " + "Washington")
# print("The length of the string is : ",len("Washington"))
# print("-"*40)

#2.	Write Python program that asks for first name and last name seprately, then print the full name.
# fname = input("Enter the first name: ")
# lname = input("Enter the last name: ")
# print("Full name is: " + fname + " " + lname)
# print("-"*40)

# 3.	Write Python program that takes “washinton” and print “Washington” (convet the first charcter to upper case).
# mystr = input("Enter the String: ")
# print(" The string with capital letter first", mystr.capitalize())
# print("-"*40)

"""
4.	Write Python program that takes “I am living in Washintgon” and find “living”
       in the string using String find function.
"""

# mystr = input("Enter the String: ")
# mysub = input("Enter substring to find: ")
# if (mystr.find(mysub)) >= 0:
#     print(mysub + " " + "is found in " + mystr)
# else: print(mysub + " " + "is NOT found in " + mystr)

"""
 5.	Write Python program that takes “I am living in Washintgon” and find first occurrence of the letter
    "m" in the string using String index function
"""
# mystr = input("Enter the String: ")
# mysub = input("Enter letter to find index: ")
# print(mystr.index(mysub))

"""
6.	Write Python program that takes “I am living in Washintgon” and replace “living” with “not living” 
    in the string using String replace function.
"""
# mystr = input("Enter the String: ")
# mysub1 = input("Enter substring to be replaced: ")
# mysub2 = input("Enter substring to be replaced with: ")
# print("The replaced new string is: " + mystr.replace(mysub1,mysub2))
"""
7.	Write Python program that takes “123456” and print True if all the characters in the text are 
    numeric using string isnumeric function.
"""
# mystr = input("Enter the String: ")
# print("Is given string " + mystr + " a numeric function ? " + str(mystr.isnumeric()))

"""
8.	Write Python program that takes “One day I buy one Tesla car” and print the number of times the 
    value "one" appears in the string using string count function.
"""
# mystr = input("Enter the String: ")
# mysub = input("Enter word to find number of occurances: ")
# print(mysub + " appears ", mystr.count(mysub), " time(s) in :" + mystr)

"""
9.	Write Python program that takes “zerorez” and revese the string, and then compres with the 
    original and print True if they both are same.
"""
# mystr = input("Enter the String: ")
# myrev = mystr[::-1]
# print("The reverse of " + mystr + " is: " + myrev)
# if mystr == myrev:
#     print("Both strings are same: True")
# else: print("Both strings are NOT same: False")

"""
10.	Write Python program that takes “I am living in Washintgon” and check if the string starts 
    with “I” using string startswith function.
"""
# mystr = input("Enter the String: ")
# mysub = input("Enter the letter to check if it startswith : ")
# if mystr.startswith(mysub):
#     print("The given string - " + mystr + ", starts with, " + mysub)
# else: print("The given string - " + mystr + ", does NOT start with, " + mysub)








"""
Int, float and complex problems
"""

# 1.	Write a Python program that takes x = 1, y = 1.1, and z = 1.2j and print it.

# x = int(input("Enter the int value (x): "))
# y = float(input("Enter the float value (y): "))
# z = complex(input("Enter the complex value (z): "))
# print(x)
# print(y)
# print(z)


# 2.	Write a Python program that takes x = 1, y = 1.1, and z = 1.2j and print their data type using type
#       function. Ex: print(type(x))

# x = int(input("Enter the int value of x: "))
# y = float(input("Enter the float value of y: "))
# z = complex(input("Enter the complex value of z: "))
# print("The x is of type: ", type(x))
# print("The y is of type: ", type(y))
# print("The z is of type: ", type(z))


# 3.	Write a Python program that takes y = 1.1, and z = “9” and cast them to int using int(y).


# y = float(input("Enter the float value of y: "))
# z = str(input("Enter the  str value of z: "))
# print("The cast int value of y: ", int(y))
# print("The cast int value of z: ", int(z))

# 4.	Write a Python program that takes y = 1.1, and z = “9” and cast them to float using float(y).

# y = float(input("Enter the float value of y: "))
# z = str(input("Enter the  str value of z: "))
# print("The cast float value of y: ", float(y))
# print("The cast float value of z: ", float(z))


# 5.	Write a Python program that takes y = 1.1, and z = “9” and cast them to string using str(y).

# y = float(input("Enter the float value of y: "))
# z = str(input("Enter the  str value of z: "))
# print("The cast str value of y: ", str(y))
# print("The cast str value of z: ", str(z))


######## Another method for 3, 4, 5 Hardcoding
# y = 1.1
# z = "9"
# print("Cast int value of y is: ", int(y))
# print("Cast int value of z is: ", int(z))             # It gives error if z = "9.0"
# print("Cast float value of y is: ", float(y))
# print("Cast float value of z is: ", float(z))
# print("Cast string value of y is: ", str(y))
# print("Cast string value of z is: ", str(z))


"""
Python Lists
"""

# 1.	Write a Python program that takes mylist = ["WA", "CA", "NY"] and add “IL” to the list.

# mylist = ["WA", "CA", "NY"]
# print("Given list is: ", mylist)
# newcity = input("Enter city to add :")
# mylist.append(newcity)
# print("Modified list is: ", mylist)

# 2.	Write a Python program that takes mylist = ["WA", "CA", "NY", “IL”] and print the list.
# mylist = ["WA", "CA", "NY", "IL"]
# print("Given list is: ", mylist)

####### Alternative
# total_cities = int(input("Enter number of cities in the list: "))
# mylist = []
# for i in range(1,total_cities+1):
#     mylist.append(input("Enter city in mylist :"))
# print(mylist)

# 3.	Write a Python program that takes mylist = ["WA", "CA", "NY", “IL”] and print
#       position/Index of CA in the list using list index function.

# total_cities = int(input("Enter number of cities in the list: "))
# mylist = []
# for i in range(1,total_cities+1):
#     mylist.append(input("Enter city in mylist :"))
# print("Given list is : ", mylist)
# city = input("The city index to be found :")
# print(" The index of " + city + " in given list is: ", mylist.index(city))


# 4.	Write a Python program that takes mylist = ["WA", "CA", "NY", “IL”] and print
#       position/index of each item in the list using list index function.

# total_cities = int(input("Enter number of cities in the list: "))
# mylist = []
# for i in range(1,total_cities+1):
#     mylist.append(input("Enter city in mylist :"))
# print("Given list is : ", mylist)
# for city in mylist:
#     print(" The index of " + city + " in given list is: ", mylist.index(city))

# 5.	Write a Python program that takes mylist = ["WA", "CA", "NY", “IL”, “WA”, “CA”, “WA”] and sort
#       the list using list sort function.

# total_cities = int(input("Enter number of cities in the list: "))
# mylist = []
# for i in range(1,total_cities+1):
#     mylist.append(input("Enter city in mylist :"))
# print("Given list is : ", mylist)
# mylist.sort()
# print("The sorted list is :", mylist)

# 6.	Write a Python program that takes mylist = ["Seattle", "Bellevue", "Redmond", “Issaquah”] and
#       print it using for loop.

# total_cities = int(input("Enter number of cities in the list: "))
# mylist = []
# for i in range(1,total_cities+1):
#     mylist.append(input("Enter city in mylist :"))
# print("Given list is : ", mylist)
# for city in mylist:
#     print(city)

# 7.	Write a Python program that takes mylist = ["WA", "CA", "NY", “IL”] and print it respective state
#        names (Ex: WA is Washington] for each item in the list.

# total_cities = int(input("Enter number of cities in the list: "))
# mylist = []
# for i in range(1,total_cities+1):
#     mylist.append(input("Enter city in mylist :"))
# print("Given list is : ", mylist)
# for city in mylist:
#     if city == "WA":
#         print("WA is Washington state")
#     elif city == "CA":
#         print("CA is California state")
#     elif city == "NY":
#         print("NY is Newyork state")
#     elif city == "IL":
#         print("IL is Illionois state")

# 8.	Write a Python program that takes mylist = ["WA", "CA", "NY", “IL”, “WA”, “CA”, “WA”]
#       and print how many times WA appeared in the list.

# total_cities = int(input("Enter number of cities in the list: "))
# mylist = []
# for i in range(1,total_cities+1):
#     mylist.append(input("Enter city in mylist :"))
# print("Given list is : ", mylist)
# choice = input("Enter the state that needs to find number of occurences :")
# occurances = mylist.count(choice)
# print("The state " + choice + " is repeated \"",occurances, "\" time(s)")

# 9.	Write a Python program that takes mylist = ["WA", "CA", "NY", “IL”, “WA”, “CA”, “WA”]
#       and print how many times WA and CA appeared in the list.

# def create_mylist(n):
#     mylist = []
#     for i in range(1, n + 1):
#         mylist.append(input("Enter item in mylist :"))
#     return mylist


# total_cities = int(input("Enter number of cities in the list: "))
# ml = create_mylist(total_cities)
# print("Given list : ",ml)
# choice1 = input("Enter the first state that needs to find number of occurences :")
# choice2 = input("Enter the second state that needs to find number of occurences :")
# print("Occurences of  ", choice1, " is : ", ml.count(choice1))
# print("Occurences of  ", choice2, " is : ", ml.count(choice2))

# 10.	Write a Python program that takes mylist = ["WA", "CA", "NY", “IL”, “WA”, “CA”, “WA”]
#       and print how many times each state appeared in the list.

# total_cities = int(input("Enter number of cities in the list: "))
# ml = create_mylist(total_cities)
# print("Given list : ",ml)
#
# for city in ml:
#     print("Occurences of  ", city, " is : ", ml.count(city))

# 11.	Write a Python program that takes mylist = [1, 2, 3, 4, 5] and print sum of all the items in the list.

# total_numbers = int(input("Enter total numbers in the list: "))
# ml = create_mylist(total_numbers)
# print("Given list : ",ml)
# sum = 0
# for number in ml:
#     sum += int(number)
# print("The sum of the numbers in list  ", sum)

# 12.	Write a Python program that takes mylist = [1, 2, 3, 4, 5] and print large number from the list.

# total_numbers = int(input("Enter total numbers in the list: "))
# ml = create_mylist(total_numbers)
# print("Given list : ",ml)
# ml.sort()
# print("The largest number in the given list is : ", ml[total_numbers-1])

# 13.	Write a Python program that takes mylist = [1, 2, 3, 4, 5] and print middle number from the list.

# total_numbers = int(input("Enter total numbers in the list: "))
# ml = create_mylist(total_numbers)
# print("Given list : ",ml)
# print("The middle number in the given list is : ", sorted(ml)[len(ml) // 2])

# 14.	Write a Python program that takes mylist = [“CAL”, “SEA”, “PIT”, “CAL”] and print the
#       string that appeared more than once.

# total_cities = int(input("Enter total numbers in the list: "))
# ml = create_mylist(total_cities)
# print("Given list : ",ml)
# for city in ml:
#     if ml.count(city) > 1:
#         print("The city  ", city, " appeared more than once. ")

# 15.	Write a Python program that takes mylist = [“CAL”, “SEA”, “PIT”, “CAL”] and remove duplicates from the list.

# total_cities = int(input("Enter total numbers in the list: "))
# ml = create_mylist(total_cities)
# print("Given list : ",ml)
# Method 1: ------------------
# ml_remove_dups = list(set(ml))
# print(ml_remove_dups)
# Method 2:-----------------
# ml_no_dupes = []
# for item in ml:
#     if item not in ml_no_dupes:
#         ml_no_dupes.append(item)
# print("The list without dupes :",ml_no_dupes)



# 16.	Write a Python program that takes mylist = [“CAL”, “SEA”, “PIT”, “CAL”, “POR”, “KEN”, “NJC”] and
#       remove all even items in the list.

# total_cities = int(input("Enter total numbers in the list: "))
# ml = create_mylist(total_cities)
# print("Given list : ",ml)

# Method 1: With slicing --------------
# print(ml[::2])

# Method 2: With new list --------------
# ml_new = []
# c = 0
# for i in ml:
#     if c % 2 == 0: # if == 1, will print numbers in even positions
#         ml_new.append(i)
#     c += 1
# print(ml_new)

# Method 3 (Without using additional list------------------------
# c = 0
# orig_len = len(ml)
# print("Original length :",orig_len)    # No need to have orig_len as len(ml) is constant in loop.
# for i in range(orig_len):
#     if c % 2 == 0: # if == 1, will print numbers in even positions
#         ml.append(ml[i])
#     c += 1
# del ml[0:5]
# for i in range(orig_len):  # Alternatively ise del ml[0::orig_len]
#     ml.pop(0)
# print(ml)

### Method 4 Without additional list..more optimized

# c = 0
# orig_len = len(ml)
# for i in range(orig_len):
#     if c % 2 == 1: # if == 1, will print numbers in even positions
#         ml.append(ml[i])
#     c += 1
# del ml[0:orig_len]
# print(ml)


#### General

# ml.insert(1,"la")   # To insert an item "la" before index ie. 1
# print(ml)
# for item in ml:              # To pop out item with index
#     pl = ml.index(item)
#     print("The index of :", item, " is :", pl)
# del ml[1]
# print(ml)
# del m1[2]
# print(ml)

# 17.	Write a Python program that takes mylist = [“CALIFORNIA”, “SEATTLE”, “PIT”]
#       and print number of characters in each item in the list.

# total_cities = int(input("Enter total numbers in the list: "))
# ml = create_mylist(total_cities)
# print("Given list : ",ml)
# for i in ml:
#     print("The number of charecters in ",i, " is: ", len(i))

# 18.	Write a Python program that takes list1 = [“WA”, “CA”] and
#       list2 = [“Washinton”, “California] and create a list3 = [“WA”, “Washington”, “CA”, “California”].

# total_cities = int(input("Enter total numbers in the list: "))
# mlist1 = create_mylist(total_cities)
# print("Given list 1: ",mlist1)
# mlist2 = create_mylist(total_cities)
# print("Given list 2: ",mlist2)
### Using 3rd list------------------
# mlist3 =[]
# for i in range(len(mlist1)):
#     mlist3.append(mlist1[i])
#     mlist3.append(mlist2[i])
# print(mlist3)
### without new list---------------------
# p = 0
# for i in range(len(mlist1)):
#     print("i value:",i)
#     mlist2.insert(p,mlist1[i])
#     p += 2
# print(mlist2)


# 19.	Write a Python program that takes mylist = [6, 2, 7, 3, 4, 5] and sort the list ascending
#       without using sort function.

# def my_sort(mlist):
#     sorted_list = []
#     while mlist:
#         min = mlist[0]
#         for x in mlist:
#             if x < min:
#                 min = x
#         sorted_list.append(min)
#         mlist.remove(min)
#     return sorted_list

# total_numbers = int(input("Enter total numbers in the list: "))
# ml = create_mylist(total_numbers)
# print("Given list : ",ml)
# sort_list = []
# while ml:
#     min = ml[0]
#     for x in ml:
#         if x < min:
#             min = x
#     sort_list.append(min)
#     ml.remove(min)
# print("The sorted list is : ",sort_list)

# 20.	Write a Python program that takes mylist = [1, 2, 3, 4, 5] and print second larget number from the list.

# total_numbers = int(input("Enter total numbers in the list: "))
# mlist = create_mylist(total_numbers)
# print("Given list : ",mlist)
# slist = my_sort(mlist)
# print(" The sorted list is : ",slist)
# print(" The second largest number is : ",slist[len(slist)-2])

"""
Tuple problems
"""

# 1.	Write a Python program that takes mytuple = ("WA", "CA", "NY") and print the tuple using for loop.
# mytuple = ("WA", "CA", "NY")
# print("The given tuple :", mytuple)
# for item in mytuple:
#     print(item)

# 2.	Write a Python program that takes mytuple = ("WA", "CA", "NY") and print first item using index.

# mytuple = ("WA", "CA", "NY")
# print("The given tuple :", mytuple)
# print("The first item in given tuple is: ", mytuple[0])

# 3.	Write a Python program that takes mytuple = ("WA", "CA", "NY") and change first item = “NJ”
# mytuple = ("WA", "CA", "NY")
# print("The given tuple :", mytuple)
# try :
#     mytuple[0] = "NJ"
# except:
#     print("Tuples are immutable. You Can't change first item")

# 4.	Write a Python program that takes mytuple = ("WA", "CA", "NY") and check if “CA” exists and print.
# mytuple = ("WA", "CA", "NY")
# print("The given tuple :", mytuple)
# city = input("Enter the city to be checked :")
# if city in mytuple:
#     print(city, " exists in mytuple provided")
# else:
#     print(city, " does NOT exist in mytuple provided")

# 5.	Write a Python program that takes mytuple = ("WA", "CA", "NY") and print length of the tuple.
# mytuple = ("WA", "CA", "NY")
# print("The given tuple :", mytuple)
# print("The length of given tuple :", len(mytuple))

"""
Set problmes
"""

# 1.	Write a Python program that takes myset = {"NFL", "Cricket", "Baseball"} and print the set.
#      Run multiple times and see if it is printing in the same order.

# myset = {"NFL", "Cricket", "Baseball"}
# print("Defined set: {\"NFL\", \"Cricket\", \"Baseball\"}")
# print("Printing given set first time: ",myset)
# print("Printing given set second time: ",myset)
# print("Printing given set third time: ",myset)

# 2.	Write a Python program that takes myset = {"NFL", "Cricket", "Baseball"} and add “Soccer” to the set.

# myset = {"NFL", "Cricket", "Baseball"}
# print("Defined set: {\"NFL\", \"Cricket\", \"Baseball\"}")
# myset.add(input("Enter item to be added in set :"))
# print("Modified set :", myset)

# 3.	Write a Python program that takes myset = {"NFL", "Cricket", "Baseball"} and remove an item
#       using pop (myset.pop) and print which item was removed.

# myset = {"NFL", "Cricket", "Baseball"}
# print("Defined set: {\"NFL\", \"Cricket\", \"Baseball\"}")
# myset.pop()
# print("Modified set :", myset)

# 4.	Write a Python program that takes myset1 = {"NFL", "Cricket", "Baseball"} myset2 = {"NFL", "Cricket", "Soccer"}
#       and print items that are different in the two sets using set.difference function.

# myset1 = {"NFL", "Cricket", "Baseball"}
# print("Defined set: {\"NFL\", \"Cricket\", \"Baseball\"}")
# myset2 = {"NFL", "Cricket", "Soccer"}
# print("Defined set: {\"NFL\", \"Cricket\", \"Soccer\"}")
# print("The difference set :", myset1.difference(myset2))
# print("The difference set :", myset2.difference(myset1))
# print("The Symmetric difference set :", myset1.symmetric_difference(myset2))

# 5.	Write a Python program that takes myset1 = {"NFL", "Cricket", "Baseball"}
#       myset2 = {"NFL", "Cricket"}  and see if myset1 is superset of myset2 using set.issuperset function.

# myset1 = {"NFL", "Cricket", "Baseball"}
# print("Defined set: {\"NFL\", \"Cricket\", \"Baseball\"}")
# myset2 = {"NFL", "Cricket", "Soccer"}
# print("Defined set: {\"NFL\", \"Cricket\", \"Soccer\"}")
# print("Is myset1 is superset of myset2 ? ", myset1.issuperset(myset2))
# myset3 = {"NFL", "Cricket"}
# print("Is myset1 is superset of myset3 ? ", myset1.issuperset(myset3))

"""
Dictionary problems
"""
# 1.	Write a Python program that takes mydict = { “Game”: “NFL”, “Team”: “Seahwaks”, “City”: “Seattle”}
#       and print mydict.
# mydict = {"Game": "NFL", "Team": "Seahawks", "City": "Seattle"}
# print(mydict)

# a.	Print the value of “Team” key using mydict[“Team”]
# print(mydict["Team"])

# b.	Print the value of “Team” key using mydict,get(“Team”)
# print(mydict.get("Team"))

# c.	Change the value of “Game” = “XFL”
# mydict["Game"] = "XFL"
# print("The modified dictionary :\n",mydict)

# d.	Print all the key names in the dictionary using for loop.
# for i in mydict:
#     print(i)

# e.	Print all the key values in the dictionary using for loop.
# for i in mydict:
#     print(mydict[i])

# f.	Check if key “Team” exists and print Yes, it exists.
# if "Team" in mydict:
#     print("Yes, Team exists in mydict")

# g.	Remove “Game” using pop method.
# mydict.pop("Game")
# print(mydict)

# h.	Add “Year” = “1980” to the mydict.
# mydict1 = {"Year": "1980"}
# mydict.update(mydict1)
# print(mydict)

# i.	Remove using popitem method (which one does it remove?)
# mydict.popitem()
# print(mydict)

# j.	Clear all the items in the mydict.
# mydict.clear()
# print(mydict)

