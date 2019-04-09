print("Exercise B4 - Python functions with dictionary")

myStateDict = {'WA': 'Washington', 'IL': 'Illionois', 'OK' : 'Okalohoma', 'TX' : 'Texas', 'FL' : 'Florida'}

def delState(stateCode):
    stateName = myStateDict.pop(stateCode)

stateCode = input("Enter the state code you want to delete from the dictionary : " )
delState(stateCode)

print("The state new state dictionary: ", myStateDict)
