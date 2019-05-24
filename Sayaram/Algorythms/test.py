array = [1,2,3,9]

def addElement(given_array):
    count = len(given_array)
    check = 1
    while count >=0:
        if given_array[count-1] >= 9:
            strnum = str(given_array[count-1] + 1)
            given_array[count-1] = int(strnum[::-1])
        else:
            given_array[count-1] += 1
            check = 0
        count -= 1
    if check == 1:
        given_array.insert(0, 1)
    return given_array

print(addElement(array))