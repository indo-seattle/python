print("Exercise 46 - Python Dictionary")

myDict = { "Game": "NFL", "Team": "Seahwaks", "City": "Seattle"}
print(myDict)


print(myDict["Team"])
print(myDict.get("Team"))

myDict["Game"] = "XFL"
print(myDict)

# Print all key names in the dictionary, one by one
for x in myDict:
  print(x)

# Print all values in the dictionary, one by one:
for x in myDict:
  print(myDict[x])

for x in myDict.values():
  print(x)

if "Team" in myDict:
  print("Yes, 'Team' is one of the keys in the myDict dictionary")

#The pop() method removes the item with the specified key name:
myDict = { "Game": "NFL", "Team": "Seahwaks", "City": "Seattle"}
myDict.pop("Game")
print(myDict)

# Adding an item to the dictionary is done by using a new index key and assigning a value to it
myDict = { "Game": "NFL", "Team": "Seahwaks", "City": "Seattle"}
myDict["Year"] = "1980"
print(myDict)

#The popitem() method removes the last inserted item (in versions before 3.7, a random item is removed instead):
myDict.popitem()
print(myDict)

#Remove all elements from the car list:
myDict.clear()
print(myDict)