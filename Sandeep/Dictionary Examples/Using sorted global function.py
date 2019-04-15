
mydict = {'Bellevue': 'Microsoft', 'Seattle' : 'Amazon','Everett':'Boeing'}

mydict['Infosys']='Bengaluru'

print(sorted(mydict.values()))


for i in range(sorted(mydict.values())):
    print(i+" started in "+mydict.keys(i))



