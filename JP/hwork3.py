import utils    # imports all functions in the module
from utils import my_sort   # Imports specifc function in module utils

# mlist = utils.create_mylist(int(input("Give No. of items to be created in list :")))
# print("Given list is : ", mlist)
# print("Sorted list is :", my_sort(mlist))



# Staircase problem
# height = int(input("Enter height of the staircase :"))
# for i in range( height + 1):
    # print("*" * i)   # for left allignment
    # print(" " * (height - i),"*" * i )    # For Right allignment
    # print(" " * int((height - i)//2),"*" * int((2 * i - 1)), " " * int((height - i)//2 ))    # For Right allignment
    # print("*" * (2*i-1))

# mlist = [10,5,60,2,20]
# print(mlist)
# mlist = utils.create_numbers_list(5)
# print(utils.find_max(mlist))








#Dictionary & using Python modules
# 1.	Write a python script that can take mydict = {‘Bellevue’: ‘Microsoft’, ‘Seattle’: ‘Amazon’, ‘Everett’:’Boeing’} and print
# o	Microsoft started in Bellevue
# o	Amazon started in Seattle
# o	Boeing started in Everett

# mydict = {
#     "Bellevue": "Microsoft",
#     "Seattle": "Amazon",
#     "Everett": "Boeing"
# }
# for i in mydict:
#     print(mydict[i], "started in", i)

# General working good.
#----------------------
# for i in mydict.values():         # To print values
#     print(i)
# for i in mydict:           # To print keys, you can laos use for i in mydict.key()
#     print(i)
# for i, j in mydict.items():       # To print key, value pairs
#     print(i,j)
# if "Bellevue" in mydict:          # To check if a key is present
#     print("Yes, Bellevue is in")
# if "Microsoft" in mydict.values():      # To check if a value is present
#     print("Yes, Microsoft is in")



# 2.	Write a python script that can take mydict = {‘Bellevue’: ‘Microsoft’, ‘Seattle’: ‘Amazon’, ‘Everett’:’Boeing’} and sort (hint: sorted global function) the dictionary and print
# o	Amazon started in Seattle
# o	Boeing started in Everett
# o	Microsoft started in Bellevue

# sorted_list = sorted(mydict, key=mydict.get, reverse=False)
# print(sorted_list)
# for k in sorted_list:
#     print(mydict[k], "started in", k)


# 3.	Write a python script that can take mydict1 = {‘House1’: 1000, ‘House2’: 3000, ‘House3’: 5000} and mydict2 = {‘House1’: 6000, ‘House3’: 8000, ‘House2’: 6000} and to combine two dictionary adding values for common keys.
# o	Output should be mydict3={‘House1’: 7000, ‘House2’: 9000, ‘House3’: 13000}

# mydict1 = {
#     "House1": 1000,
#     "House2": 3000,
#     "House3": 5000
# }
#
# mydict2 = {
#     "House1": 6000,
#     "House3": 8000,
#     "House2": 6000
# }
#
# mydict3 = {}
# for k in mydict1:
#     mydict3[k] = mydict1[k] + mydict2[k]
#
# print(mydict3)



# 4.	Write a python script that can take mydict={‘House1’: 7000, ‘House2’: 9000, ‘House3’: 13000} and print two
#       largest values in the dictionary.
# o	Hint: use nlargest function in heapq module

# from heapq import nlargest as nl
#
# mydict1 = {
#     "House1": 7000,
#     "House2": 9000,
#     "House3": 13000
# }
# print("\nGiven dictionary is :", mydict1)
# TwoHighest = nl(2,mydict1,key=mydict1.get)  # Its sorts values
# TwoHighest = nl(2,mydict1)   # It sorts keys only, not values
# print("Two highest values :", TwoHighest)
# print("\nKeys   : Values" )
#
# for key in TwoHighest:
#     print(key, ":" , mydict1.get(key))

#### To print 2 largest numbers in list
# mlist = [10,20,1,4,39]
# print(nl(2,mlist))



# 5.	Write a python script that can take x = 3, using loops create three key and value pairs disctionary
# {1:1, 2:4, 3:6}. If key = 1, value is 1+1, for 2 value is 2+2, etc.

# x = int(input("Give number of items in dictionary"))
# mydict1 = {}
#
# for i in range(1, x + 1):
#     mydict1[i] = i * 2
#     print(f"i:{i} and val:{mydict1[i]}")
#
# print(mydict1)

# 6.	Write a python script that can take x = 3, using loops create key and value pairs dictionary
# {4:2, 9:3, 16:4}. If key = 4, value sqrt(4) is 2, for 9 value is 3, etc.
#  o	Hint: use pow function in Math module

# from math import pow

# x = int(input("Give number of items in dictionary"))
# mydict1 = {}

#### display {2,4 3:9}
# for i in range(2, x + 2):
#     mydict1[i] = int(pow(i,2))
# print(mydict1)


#### To display {4:2, 9:3}
# ml = []
# for i in range(2,x+2):
#     ml.append(int(pow(i,2)))
# print(ml)
#
# for i in ml:
#     mydict1[i] = int(pow(i,1/2))
# print(mydict1)



# 7.	Write a python script that can take x = 3, using loops create key and value pairs disctionary {1:1, 2:8, 3:27}. If key = 2, value pow(2) is 8, for 3 value is 27, etc.
# o	Hint: use pow function in Math module

#### display {1:1, 2,8 3:27}
# for i in range(1, x + 1):
#     mydict1[i] = int(pow(i,3))
# print(mydict1)


########### Functions

# 1.	Create a function mystatenamelist  that can take string statename parameter and add to a list. Call that
# function and add up to 5 states.

##### This function accepts number of states
# def my_state_name_list(n):
#     ml = []
#     while n > 0:
#         s = input("Enter your state")
#         ml.append(s)
#         n -= 1
#     return ml

# no_of_states = int(input("Howmany states you want to add ? "))
# mlist = my_state_name_list(no_of_states)
# print("Here is the list of states given: \n", mlist)

##### This function accepts state name
# def my_state_name_list(sn):
#     ml.append(sn)
#     return ml

# ml = []
# no_of_sates = int(input("Enter number of states you want to add :"))
# for state in range(no_of_sates):
#     state_name = input("Enter state name :")
#     mlist = my_state_name_list(state_name)
# print(mlist)

# no_of_states = int(input("Howmany states you want to add ? "))
# mlist = my_state_name_list(no_of_states)
# print("Here is the list of states given: \n", mlist)




# 2.	Create a function mystateinfodict that can take string statename and string statecode parameters and
# add to a dictionary (key = statecode, value = statename) and add upto 5 states.

###### This functiona takes no.of states and create dictionary
# def my_state_info_dict(n):
#     md = {}
#     for i in range(n):
#         sc = input("Enter your state code")
#         sn = input("Enter your state name")
#         md[sc] = sn
#     return md

# no_of_items = int(input("Howmany items you want to add in dictionary ? "))
# mydict1 = my_state_info_dict(no_of_items)
# print(mydict1)

######### Function takes state code and state name and creates dictionary

# def my_state_info_dict(sc,sn):
#     md[sc] = sn
#     return md
#
# md = {}
# no_of_states = int(input("Howmany states you want to add ? "))
# for every_state in range(no_of_states):
#     scode = input("Enter your state code")
#     sname = input("Enter your state name")
#     mydict1 = my_state_info_dict(scode,sname)
# print("The dictionary is :", mydict1)




# 3.	Create a function findmystatename that can take statecode parameter and return statename for the 5
#       states you created in problem 2.

##### without using function
# state_code = input("Enter the state code : ")
# print(" The state name of {0} is : {1}".format(state_code,mydict1.get(state_code)))

######## With function
# def find_my_state_name(sc):
#     return mydict1.get(sc)

# state_code = input("Enter state code : ")
# state_name = find_my_state_name(state_code)
# print(" The state name of {0} is : {1}".format(state_code,state_name))



# 4.	Create a function delmystatename that can take statecode parameter and delete statename
#       if it exists in the list you created in problem 2.

# def del_my_state_name(sc):
#     return mydict1.pop(sc)
#
# state_code = input("Enter state code to be deleted : ")
# del_my_state_name(state_code)
# print("The modified dictionary after entry for {} is deleted.".format(state_code))
# print(mydict1)



# 5.	Write a Python function that accepts a string parameter and calculate the number of upper case letters and
#       lower case letters and returns it.


# def string_char_case(ms):
#     count_upper = 0
#     count_lower = 0
#     count_other = 0
#     for i in ms:
#         if i.isupper():
#             count_upper += 1
#         elif i.islower():
#             count_lower += 1
#         else:
#             count_other += 1
#     return count_upper, count_lower, count_other
#
# mstring = input("Enter the string :")
# u,l,ot = string_char_case(mstring)
# print("Upper case letters in given string  :", u)
# print("Lower case letters in given string  :", l)
# print("Neither upper nor lower case letters in given string  :", ot)


# 6.	Write a Python function sumoflist that can take a list with all numbers and calculate the sum of a list of
#       numbers and returns it. Use recursive function, if possible.

# import utils
#
#
# def sum_of_list(ml):
#     if len(ml) == 1:
#         return ml[0]
#     else:
#         return ml[0] + sum_of_list(ml[1:])
#
#
# num = int(input("Howmany numbers you want in the list ? "))
# mlist = utils.create_numbers_list(num)
# my_sum = sum_of_list(mlist)
# print("The sum of the numbers in the list {} ===>  {}".format(mlist,my_sum))


# 7.	Write a python function myfactorial that takes n as parameter to calculate the factorial number and returns it.
# Use recursive function, if possible.

# def my_factorial(n):
#     if n == 0 or n == 1:
#         return 1
#     else:
#         return n * my_factorial(n-1)
#
# num = int(input("Enter the number to find factorial value : "))
# print("The factorial of {} ==> {} ".format(num,my_factorial(num)))
# print("The digits in factorial are :",len(str(my_factorial(num))))

########## Factorial using for loop
fact = 1
n = int(input("Enter the number to find factorial value : "))
while n > 1:
    fact = fact * n
    n -= 1

print("The factorial of {} ==> {} ".format(n,fact))
print("The digits in factorial are :",len(str(fact)))
