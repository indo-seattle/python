print("Exercise A1 - Python Dictionary & using python modules")
mydict = {'bellevue': 'Microsoft', 'Seattle': 'Amazon', 'Everett':'Boeing'}

for mycity in mydict:
    # print('Key :', mycity)
    # print('Value :', mydict[mycity])

    print ( mydict[mycity].capitalize(), ' started in ', mycity.capitalize())