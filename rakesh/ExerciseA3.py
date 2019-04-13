print("Exercise A3 - Python Dictionary & using python modules - Dictionary Sort")
print("In Python 3.5, you can merge two or more dictionaries in a single statement by unpacking the new dictionaries into a new dictionary.")

dict1 = {'House1': 1000, 'House2': 3000, 'House3': 5000}
dict2 = {'House1': 6000, 'House3': 8000, 'House2': 6000}

dict = {**dict2, **dict1}
print(dict)

dict = {**dict1, **dict2}
print(dict)

for key in dict2:
    if key in dict1:
        dict2[key] = dict2[key] + dict1[key]

dict3 = {**dict1, **dict2}


print(dict3)


