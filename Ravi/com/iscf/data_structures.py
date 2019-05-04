# # List is a collection which is ordered and changeable. Allows duplicate members.
# # Example: list_of_even_numbers = [2, 4, 6, 8, 10]
#
# Note: Write in one Pycharm file and check-in Git.
# Problem
# Hint
# Create a list of week days (Sunday to Saturday).
week_days = ["Sunday","Monday","Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
print(week_days)

#
#
# Print 3rd item of the list.
# Use List[index]
print(week_days[2])

# Print length of the list.
# Use len()
print(len(week_days))

# Remove Friday from the list.
# Use list.pop()
print ( str(week_days.pop(5)))
print(week_days)

# Add Friday to the list before Saturday
# Use list.append()
week_days.insert(5,"Friday")
print(week_days)

# Add another Monday value to the list
# Use list.insert()
week_days.append("Monday")
print(week_days)

# Print number of times Monday occured in the list.
# Use list.count()
print( week_days.count("Monday"))

# Remove Monday from the list
# Use list.remove()
for day in week_days:
    if (day == "Monday"):
        week_days.remove("Monday")
print(week_days)

# Print the list by reversing it
# Use list.reverse()
week_days.reverse()
print(week_days)

# Print the list by sorting ascending and descending
# Use list sort()
week_days.sort()
print(week_days)

# Print all the items in the list using for loop
# For loop
for day in week_days:
    print(day)

# Print all the index values for each item in the list (loop)
# For loop
for day in week_days:
    print(week_days.index(day))

# Print all the items from last to first in the list (loop)
# While loop & Len function

number_of_days = len(week_days)
while (number_of_days - 1  >= 0):
    print(week_days[number_of_days -1 ])
    number_of_days -= 1

# Print all odd items in the list
# For loop & mod
number_of_days = len(week_days)
for day_number in range(number_of_days):
    if (day_number % 2 != 0 ):
        print(week_days[day_number])


# Print all the even items in the list
# For loop & mod
number_of_days = len(week_days)
for day_number in range(number_of_days):
    if (day_number % 2 == 0 ):
        print(week_days[day_number])

# Print “Thursday is the fifth day of the week” going through the loop and if list has Thursday
# For loop & IF condition
for day in week_days:
    if ( day == "Thursday"):
        print("Thursday is the fifth day of the week")

# Copy this list to another new list
# list.copy()
print(week_days.copy())

# Merge both lists to first list
# list.extend()
week_days2 = week_days.copy()
week_days.extend(week_days2)
print(week_days)

# Clear all the items in the list
# list.clear()
week_days.clear()
print(week_days)

# Print type of the list class
# Use type
print(type(week_days))
# List is a data structure. In computer science, a data structure is a data organization, management and storage format that enables efficient access and modification. A data structure is a collection of data values, the relationships among them, and the functions or operations that can be applied to the data.
# Dictionary is a collection which is unordered, changeable and indexed. No duplicate members.
#
countries_population = {"India": "1.3", "China": "1.4", "USA": "0.32", "Indonesia": "0.26"}
#
# Note: Write in one Pycharm file and check-in Git.
# Problem
# Hint
# Create a dict variable as stated above.
#
#
# Print value of key India
# Use dict[key]
print(countries_population["India"])
# Print length of the list
# Use len()
print(len(countries_population))
# Print value of key China
# Use dict.get()
print(countries_population.get("China"))
# Return all the keys of the dict
# Use dict.keys()
print(countries_population.keys())
# Remove key = Indonesia from the list
# Use dict.pop()
print(countries_population.pop("Indonesia"))
print(countries_population)
# Add new items Canada = 0.03 billion
# Use dict.update()
countries_population.update({"Canada" : "0.03"})
print(countries_population)
# Return all the values into the list
# Use dict.values()
print(countries_population.values())
# Print all the dict keys in the list (loop)
# Use for loop
for k,v in countries_population.items():
    print(k)
# Print all the dict values in the list (loop)
# Use for loop
for k,v in countries_population.items():
    print(v)
# Print the values of countries USA and India
# Use for loop and if
for k,v in countries_population.items():
    if ( k == "USA" or k == "India"):
        print(v)
# Print the values of countries except for USA
# Use for loop and if
for k,v in countries_population.items():
    if ( k != "USA"):
        print(v)
# Print all the countries with value over billion (>1.0)
# Use for loop and if
for k,v in countries_population.items():
    if ( float(v) > 1.0 ):
        print(k)
# Print all the countries with value under billion (<1.0)
# Use for loop and if
for k,v in countries_population.items():
    if ( float(v) < 1.0 ):
        print(k)
# Print all the countries that starts with “I”
# Use for loop and str.startswith()
for k,v in countries_population.items():
    if ( k.startswith("I") ):
        print(k)
# Print all the countries that ends with “a”
# Use for loop and str.endswith()
for k,v in countries_population.items():
    if ( k.endswith("a") ):
        print(k)
#
# Dict is a data structure. The unique nature of Dict (Dictionary) data structure is that it stores in key-value pair. Every key associated with a value, a association of data. Key serves as a unique identifier in the dictionary. Dict doesn’t allow duplicate keys so every pair of the key-value can be uniquely identified with key.
# #


