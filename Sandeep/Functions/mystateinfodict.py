mydict={}
def mystateinfodict(stateCode, stateName):
    mydict[stateCode]=stateName
    print(mydict)

mystateinfodict('CA','California')
mystateinfodict('WA','Washington')
mystateinfodict('FL','Florida')
mystateinfodict('NY','NewYork')
mystateinfodict('TX','TEXAS')

#import findmystatename
#print(findmystatename.findmystatename('CA'))