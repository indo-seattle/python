

from operator import itemgetter
from collections import OrderedDict
from heapq import nlargest
from math import pow
from math import factorial


# mydict = {"Bellevue": "Microsoft", "Seattle": "Amazon", "Everett":"Boeing"}
#
# print('original')
# print('--------')
# for city,company in mydict.items():
#     print(company + " started in " + city)


# print('')
# print('sort by city')
# print('------------')
# sorted_dict3 = sorted(mydict, key=itemgetter(0))
# print ( sorted_dict3 )
# for city in sorted_dict3:
#     print(mydict.get(city) + " started in " + city)
#
#
# print('')
# print('sort by company')
# print('---------------')
# sorted_dict2 = sorted(mydict, key=itemgetter(2))
# print ( sorted_dict2 )
# for city in sorted_dict2:
#     print(mydict.get(city) + " started in " + city )
#
# print('')
# print('sort by city reversed')
# print('---------------------')
# sorted_dict4 = sorted(mydict, key=itemgetter(0), reverse=True)
# print ( sorted_dict4 )
# for city in sorted_dict4:
#     print(mydict.get(city) + " started in " + city)
#
# print('')
# print('sort by company reversed')
# print('------------------------')
# sorted_dict5 = sorted(mydict, key=itemgetter(2), reverse=True)
# print ( sorted_dict5 )
# for city in sorted_dict5:
#     print(mydict.get(city) + " started in " + city)


# print('')
# print('sort by company reversed')
# print('------------------------')
# od = OrderedDict(sorted(mydict.items(), key=lambda x : x[1], reverse=True))
# for city,company in od.items():
#     print( company + " started in " + city )
#
# print('')
# print('sort by company')
# print('------------------------')
# od = OrderedDict(sorted(mydict.items(), key=lambda x: x[1]))
# for city, company in od.items():
#     print(company + " started in " + city)
#
# print('')
# print('sort by city reversed')
# print('------------------------')
# od = OrderedDict(sorted(mydict.items(), key=lambda x: x[0], reverse=True))
# for city, company in od.items():
#     print(company + " started in " + city)
#
# print('')
# print('sort by city')
# print('------------------------')
# od = OrderedDict(sorted(mydict.items(), key=lambda x: x[0]))
# for city, company in od.items():
#     print(company + " started in " + city)

# mydict1 = {"House1": 1000 , "House2": 3000, "House3": 5000}
# mydict2 = {"House1": 6000 ,  "House3": 8000, "House2": 6000}
# dict3={}
# for k,v in mydict1.items():
#     for k1,v1 in mydict2.items():
#         if (k==k1):
#             v3 = v+v1
#             dict3[k]=v3
#             break
# print(dict3)
#
# for k,v in (nlargest(2,dict3.items(),key=lambda x:x[1])):
#     print (" largest house :: " + k + " value is :: " + str(v) )


# x = int( input() )
# d={}
# for i in range(1,x+1):
#     d[i]=i+i
#
# print(d)

# x = int( input() )
# d={}
# for i in range(2,x+1):
#     d[int(pow(i,2))]=i
#
# print(d)

# x = int( input() )
# d={}
# for i in range(1,x+1):
#     d[i]=int(pow(i,i))
#
# print(d)

# lst=[]
# def mystatenamelist(statename):
 #   lst.append(statename)

# print("please enter number of names")
# x = int(input())
# for name in range(x):
#     print("please enter name")
#     n = input()
#     mystatenamelist(n)
#
# print(lst)


# mydict={}
# def mystatenamedict(statecode,statename):
#     mydict[statecode]=statename
#
# print("please enter number of names")
# x = int(input())
# for name in range(x):
#     print("please enter state code ")
#     m = input()
#     print("please enter state name ")
#     n = input()
#     mystatenamedict(m,n)
#
# print(mydict)

# mydict={'wa': 'washington', 'tx': 'texas', 'ca': 'california', 'or': 'oregon'}
# lst=['washington', 'california', 'texas']
#
# def delstatename(statecode):
#     try:
#         x = mydict.get(statecode)
#         print("statename to be removed is:: " + x)
#         lst.remove(x)
#         print("list after removal "+ str(lst))
#     except BaseException as e:
#         print("statename not found in the list " + str(e))
#
#
# print("please enter state code to delete ")
# scode = input()
# delstatename(scode)

# s = input()
# upper_count=0
# lower_count=0
#
# for i in s.strip():
#     print(i)
#     if i.isupper():
#         upper_count += 1
#     if i.islower():
#         lower_count += 1
#
# print( " uppercase count is ::: " + str(upper_count) + " and lowercase count is ::: "+ str(lower_count))


# print("enter how many numbers?")
# x = int(input())
# lst = []
# totalcount=0
#
# def buildlst():
#     for i in range(x):
#         print( "Enter Number " + str(i+1) + " to add :: " )
#         p = int(input())
#         lst.append(p)
#     print(lst)
#
# # def sumoflist(list):
# #     global totalcount
# #     for j in range(len(lst)):
# #         totalcount =  totalcount + lst[j]
#
# def sumoflistrec(list):
#
#     if (len(list)!=0):
#          return int(list.pop(0)) + sumoflistrec(list)
#     else:
#         return 0
#
# buildlst()
# totalcount = sumoflistrec(lst)
#
# print("total count is ::" + str(totalcount) )


# def myfactorial(n):
#     return factorial(n)
#
# def myfact(n):
#     if (n==1 or n==0):
#         return 1
#     else:
#         return n * myfact(n-1)
#
# def fact(n):
#     if (n == 1 or n == 0):
#         return 1
#     f=1
#     while (n> 1):
#         f = f*(n)
#         n = n-1
#     return f
#
# print("enter a number:")
# x = int(input())
# #print ( str(myfactorial(x)))
# # print( str (myfact(x)))
# print( str (fact(x)))

