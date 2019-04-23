# List is a collection which is ordered and changeable. Allows duplicate members.
# Example: list_of_even_numbers = [2, 4, 6, 8, 10]
#
# Note: Write in one Pycharm file and check-in Git.
# Problem
# Hint
# 1.  Create a list of week days (Sunday to Saturday).

# list_of_week_days = ['Sunday','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday']

# 2. Print 3rd item of the list.
# Use List[index]

# print(list_of_week_days[2])

# 3. Print length of the list.
# Use len()

# print(len(list_of_week_days))


# 4. Remove Friday from the list.
# Use list.pop()

# list_of_week_days.pop(5)
# print("List of Weekdays after popping Friday \n", list_of_week_days)

# 5. Add Friday to the list before Saturday
# Use list.append()

# list_of_week_days.append('Friday')
# print("List of Weekdays after adding Friday\n", list_of_week_days)

# 6. Add another Monday value to the list
# Use list.insert()

# list_of_week_days.insert(2,'Monday')
# print(list_of_week_days)

# 7. Print number of times Monday occured in the list.
# Use list.count()

# my_count = list_of_week_days.count('Monday')
# print("Monday repeated {} times".format(my_count))

# 8. Remove Monday from the list
# Use list.remove()

# list_of_week_days.remove('Monday')
# print(list_of_week_days)

# 9. Print the list by reversing it
# Use list.reverse()

# list_of_week_days.reverse()
# print(list_of_week_days)

# 10. Print the list by sorting ascending and descending
# Use list sort()

# 11. list_of_week_days.sort()
# # print(list_of_week_days)

# list_of_week_days.sort(reverse = True)
# print(list_of_week_days)

# 12. Print all the items in the list using for loop
# For loop

# for day in list_of_week_days:
#     print(day)


# 13. Print all the index values for each item in the list (loop)
# For loop

# for day in list_of_week_days:
#     print("The index of {} is : {} ".format(day,list_of_week_days.index(day)))

# 14. Print all the items from last to first in the list (loop)
# While loop & Len function

# n = len(list_of_week_days)
# while n > 0:
#     print(list_of_week_days[n-1])
#     n-= 1


# 15. Print all odd items in the list
# For loop & mod

# n = len(list_of_week_days)
# for i in range(n):
#     if i % 2 == 0:
#         print("{} is at position {}".format(list_of_week_days[i],i+1))


# 16. Print all the even items in the list
# For loop & mod

# n = len(list_of_week_days)
# for i in range(n):
#     if i % 2 == 1:
#         print("{} is at position {}".format(list_of_week_days[i],i+1))


# 17. Print “Thursday is the fifth day of the week” going through the loop and if list has Thursday
# For loop & IF condition

# n = len(list_of_week_days)
# for i in range(n):
#     if list_of_week_days[i] == 'Thursday':
#         print("{} is at position {}".format(list_of_week_days[i],i+1))



# 18. Copy this list to another new list
# list.copy()

# my_list = list_of_week_days.copy()
# print(my_list)

# 19. Merge both lists to first list
# list.extend()

# list_of_week_days.extend(my_list)
# print(list_of_week_days)


# 20. Clear all the items in the list
# list.clear()

# list_of_week_days.clear()
# print(list_of_week_days)

# 21. Print type of the list class
# Use type

# print(type(list_of_week_days))


# List is a data structure. In computer science, a data structure is a data organization, management and storage format that
# enables efficient access and modification. A data structure is a collection of data values, the relationships among them,
# and the functions or operations that can be applied to the data.
# Dictionary is a collection which is unordered, changeable and indexed. No duplicate members.
#
# countries_population = {“India”: ”1.3”, “China”: “1.4”, “USA”: “0.32”, “Indonesia”: “0.26”}
#
# Note: Write in one Pycharm file and check-in Git.
# Problem
# Hint
# 1. Create a dict variable as stated above.
#

countries_population = {"India": "1.3", "China": "1.4", "USA": "0.32", "Indonesia": "0.26"}

#
# 2. Print value of key India
# Use dict[key]

# print(countries_population["India"])


# 3. Print length of the list
# Use len()

# print("The length of defined dictionary: ",len(countries_population))

# 4. Print value of key China
# Use dict.get()

# print("The value of key china is : ", countries_population.get("China"))


# 5. Return all the keys of the dict
# Use dict.keys()

# print("The keys of the dict", countries_population.keys())

# 6. Remove key = Indonesia from the list
# Use dict.pop()

# countries_population.pop("Indonesia")
# print(countries_population)

# 7. Add new items Canada = 0.03 billion
# Use dict.update()

# countries_population.update({"Canada": "0.03"})
# print(countries_population)

# 8. Return all the values into the list
# Use dict.values()

# my_dict_values = countries_population.values()
# print(my_dict_values)

# 9. Print all the dict keys in the list (loop)
# Use for loop

# for item in countries_population:
#     print(item)

# print(countries_population.keys())  # ---> To print keys in a list

# 10. Print all the dict values in the list (loop)
# Use for loop

# for item in countries_population:
#     print(countries_population[item])


# 11. Print the values of countries USA and India
# Use for loop and if

# for item in countries_population:
#     if item == "USA" or item == "India":
#         print("The value of {} is: {}".format(item,countries_population[item]))

# 12. Print the values of countries except for USA
# Use for loop and if

# for item in countries_population:
#     if item != "USA":
#         print("The value of {} is: {}".format(item,countries_population[item]))

# 13. Print all the countries with value over billion (>1.0)
# Use for loop and if

# for item in countries_population:
#     if float(countries_population[item]) > 1.0:
#         print("The value of {} is: {}".format(item,countries_population[item]))



# 14. Print all the countries with value under billion (<1.0)
# Use for loop and if

# for item in countries_population:
#     if float(countries_population[item]) < 1.0:
#         print("The value of {} is: {}".format(item,countries_population[item]))


# 15. Print all the countries that starts with “I”
# Use for loop and str.startswith()

# for item in countries_population:
#     if item.startswith("I"):
#         print("{} country starts with I: ".format(item))

# 16. Print all the countries that ends with “a”
# Use for loop and str.endswith()

# for item in countries_population:
#     if item.endswith("a"):
#         print("{} - ends with a: ".format(item))


# Dict is a data structure. The unique nature of Dict (Dictionary) data structure is that it stores in key-value pair.
# Every key associated with a value, a association of data. Key serves as a unique identifier in the dictionary.
# Dict doesn’t allow duplicate keys so every pair of the key-value can be uniquely identified with key.