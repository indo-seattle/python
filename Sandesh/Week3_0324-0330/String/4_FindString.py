string = "I'm living in Washington"
y = input("Please enter the string you want to find : ")
x = string.find(y)
if x == -1:
    print ("Sorry, couldn't find the string")
else:
    print ("I found the string you're looking for which is character", x)