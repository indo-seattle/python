print("Exercise A6 - Python Dictionary & using python modules - Dictionary")

from math import pow

x = 3

# Empty dict
myDict = {}
myDict1 = {}

for x in range(2,5):
       #myDict[x] = int(pow(x,x))
       myDict1[x] = int(pow(x, 2))
       myDict[int(pow(x, 2))] = x

print(myDict)
print(myDict1)
