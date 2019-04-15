mydict1 = {'House1': 1000, 'House2': 3000, 'House3': 5000}

mydict2 = {'House1': 6000, 'House3':8000 ,'House2': 6000}

mydict3={}

for i in mydict1:
    for j in mydict2:
        if(i==j):
            mydict3[i]=mydict1[i]+mydict2[j]

print(mydict3)