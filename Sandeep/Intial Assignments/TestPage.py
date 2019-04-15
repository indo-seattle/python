#print(1/0)

list_of_days ={'Sunday','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday'}

try:
    if(list_of_days.remove('Sunday') is None):
        raise Exception('Deleting from the Week Days list is not allowed')

except:


