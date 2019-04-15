myset = {"NFL", "Cricket", "Baseball"}
#for i in myset:
    #print(i)

myset.add("Soccer")



myset.pop()

#for i in myset:
 #   print(i)


myset1={"NFL", "Cricket", "Baseball"}
myset2={"NFL", "Cricket", "Soccer"}

print(set.difference(myset1,myset2))
print(set.difference(myset2,myset1))

myset3={"NFL", "Cricket", "Baseball"}
myset4={"NFL", "Cricket"}

if(myset3.issuperset(myset4)):
    print("Yes")




