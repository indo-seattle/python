print("Exercise B1 - Python functions with list")

myStateList = []
def myStateListFunction(x):
    for x in range(x):
       state = input("Enter state name:")
       myStateList.append(state)

x = int(input("Enter the number of states to add to list : " ))
myStateListFunction(x)
print(myStateList)