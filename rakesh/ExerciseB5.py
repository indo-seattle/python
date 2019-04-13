print("Exercise B5 - Python functions")

def myFunct(x):
    lowerCase = 0
    upperCase = 0
    for i in x:
        if (i.islower()):
            lowerCase = lowerCase + 1
        elif (i.isupper()):
            upperCase = upperCase + 1
    return(upperCase, lowerCase)

x = input("Enter a string: ")

uppercase,lowercase = myFunct(x)

print("Upper Case leeters in the string provided: ", uppercase)
print("Lower Case leeters in the string provided: ", lowercase)
