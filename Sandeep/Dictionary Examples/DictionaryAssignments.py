mydict = { "Game": "NFL", "Team": "Seahwaks", "City": "Seattle"}

print(mydict)

print(mydict['Team'])

print(mydict.get('Team'))

mydict['Game'] ='XFL'

print(mydict)

for i in mydict:
    print(i)

for i in mydict:
    print(mydict[i])

for i in mydict:
    if(i=="Team"):
        print("Yes, Team exists")

mydict.pop("Game")

print(mydict)

mydict['Year']=1980

print(mydict)

mydict.popitem()
print(mydict)

mydict.clear()
print("Last")
print(mydict)


