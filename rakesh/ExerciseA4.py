print("Exercise A4 - Python Dictionary & using python modules - Dictionary Sort")

print("Python heapq module can be used to find N largest or smallest items from collections. It has two functions to help with – nlargest() nsmalles()")
print("\n")

from heapq import nlargest
mydict={'House1': 7000, 'House2': 9000, 'House3': 13000,'House5': 15000}

print(nlargest(2, mydict))
print(nlargest(3, mydict.values()))


