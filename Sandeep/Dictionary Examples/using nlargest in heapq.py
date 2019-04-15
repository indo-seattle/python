import heapq
mydict ={'House1': 7000, 'House2': 9000, 'House3': 13000}

today = (heapq.nlargest(2,mydict))

for i in today:
    print(mydict[i])
