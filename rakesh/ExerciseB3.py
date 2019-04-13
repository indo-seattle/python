print("Exercise B3 - Python functions with dictionary")

# myStateDict = {}

myStateDict = {'WA': 'Washington', 'IL': 'Illionois', 'OK' : 'Okalohoma', 'TX' : 'Texas', 'FL' : 'Florida'}

def myStateDicFunction(x):
    for x in range(x):
       stateKey = input("Enter state code:")
       stateValue = input("Enter state name:")
       myStateDict[stateKey] = stateValue

def findMyStateName(stateCode):
    stateName = myStateDict.get(stateCode)
    return stateName


#x = int(input("Enter the number of states to add to list : " ))
#myStateDicFunction(x)
#print(myStateDict)

stateCode = input("Enter the state code you want to find in the dictionary : " )
stateName = findMyStateName(stateCode)

print("The state name is : ", stateName)




