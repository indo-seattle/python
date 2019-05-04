# EXERCISES RELATED TO DICTIONARY
countries_population = {"India": 1.3, "China": 1.4, "USA": 0.32, "Indonesia": 0.26}

#Print value of key India
for i in countries_population:
    if i == 'India':
        print("Population of India is", countries_population[i])

#Print length of the list
print("Length of list is", len(countries_population))

#Print value of key China
for i in countries_population:
    if i == 'China':
        print("Value of China is", countries_population.get(i))

#Return all the keys of the dict
for i in countries_population.keys():
    print(i)

#Remove key = Indonesia from the list
countries_population.pop('Indonesia')
print(countries_population)

#Add new items Canada = 0.03 billion
countries_population.update({"Canada":0.03})
print(countries_population)

#Return all the values into the list
print("Values in list is:", countries_population.values())

#Print all the dict keys in the list (loop)
for i in countries_population:
    print("Key is: ", i)

#Print all the dict values in the list (loop)
for i in countries_population.values():
    print("Value is: ", i)

#Print the values of countries USA and India
for i in countries_population:
    if i == 'USA' or i == 'India':
        print(i, "value is", countries_population[i])

#Print the values of countries except for USA
for i in countries_population:
    if i != 'USA':
        print(i, "value is", countries_population[i])

#Print all the countries with value over billion (>1.0)
for j in countries_population.values():
    for i in countries_population:
        if j > 1.0:
            print(i)

#Print all the countries with value under billion (<1.0)
for j in countries_population.values():
    for i in countries_population:
        if j < 1.0:
            print(i)

print(countries_population)

#Print all the countries that starts with “I”
for i in countries_population:
    if i.startswith("I"):
        print("Country that start with I:", i)

#Print all the countries that ends with “a”
for i in countries_population:
    if i.endswith("a"):
        print("Country that ends with a:", i)
