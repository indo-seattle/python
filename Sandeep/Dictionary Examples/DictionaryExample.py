print("Hello")
mylist = ["CALIFORNIA", "SEATTLE", "PIT"]

for i in mylist:
    print("Length of "+i+":"+str(len(i)))

list1 = ["WA","CA"]
list2 = ["Washington","California"]

list3 =[]

for i in list1:
    for j in list2:
        if(list1.index(i)==list2.index(j)):
            list3.append(i)
            list3.append(j)

for i in list3:
    print(i)






