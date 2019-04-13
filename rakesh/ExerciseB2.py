print("Exercise B2 - Python functions with dictionary")

myStateDict = {}
def myStateDicFunction(x):
    for x in range(x):
       stateKey = input("Enter state code:")
       stateValue = input("Enter state name:")
       myStateDict[stateKey] = stateValue

x = int(input("Enter the number of states to add to list : " ))
myStateDicFunction(x)
print(myStateDict)