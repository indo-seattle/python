import mystateinfodict

def findmystatename(StateCode):
    #mydict={'CA':'California','WA':'Washnigton','FL':'Florida','NewYork':'NY'}
    mystateinfodict.mystateinfodict('ID','IDAHO')
    if (StateCode in mystateinfodict.mydict):
        return(mydict[StateCode])

print(findmystatename('CA'))
