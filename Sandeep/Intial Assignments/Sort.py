mylist = [6, 2, 7,8, 3, 4, 5,8]
newlist=[]
n=0
length=len(mylist)
while(n<length):
    for i in mylist:
        lest = mylist[0]
        if(i >=lest):
            grt=i
    newlist.append(grt)
    mylist.remove(grt)
    n=n+1

for i in newlist:
    print(i)



