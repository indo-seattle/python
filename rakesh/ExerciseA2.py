print("Exercise A2 - Python Dictionary & using python modules - Dictionary Sort")
print()

import operator

mydict = {'Bellevue': 'Microsoft', 'Seattle': 'Amazon', 'Everett':'Boeing'}

mydictSorted = sorted(mydict.values())

print(mydict)
print(mydictSorted)

for x in mydictSorted:
    print(x)
    print(x, ' started in ', mydict.get(x))