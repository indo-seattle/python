print("Exercise A7 - Python Dictionary & using python modules - Dictionary")

from math import pow

x = 3

# Empty dict
myDict = {}
myDict1 = {}

for x in range(1,5):
    myDict[x] = int(pow(x, 3))

print(myDict)
