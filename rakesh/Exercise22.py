print("Exercise 22 - Collection Data Types - Dictionary")
print("A dictionary is a collection which is unordered, changeable and indexed. In Python dictionaries are written with curly brackets, and they have keys and values.")

myDict = {"WA":"Washington",
          "IL": "Illinois" ,
          "NY" : "New York",
          "CA" :"California"}

print(myDict)

for x in myDict:
    print(x)

myDict = {"Washington" : "WA",
          "Illinois" : "IL" ,
          "New York" : "NY",
          "California": "CA"}

print(myDict)

for x in myDict:
    print(x)
