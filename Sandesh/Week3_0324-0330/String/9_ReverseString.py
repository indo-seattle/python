string = input("Enter the string which needs to reversed : ")
reversestring = string[::-1]
print("Original String : ", string)
print("Reversed String : ", reversestring)
if string == reversestring:
    print ("Reverse and original are the same")
else:
    print ("Reverse and original are NOT same")

