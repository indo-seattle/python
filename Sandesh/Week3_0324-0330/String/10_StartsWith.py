s = "I am living in Washington"
findcharacter = input("Please enter the character you want to check using start with : ")
y = s.startswith(findcharacter)
if y == True:
    print ("The sring start with the character you entered")
else:
    print ("The string DOES NOT starts with the character")