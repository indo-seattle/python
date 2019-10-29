#Write Python program that takes “I am living in Washintgon” and find first occurrence of the letter "m" in the string using String index function.
str = input("Enter a string: ")
occurance = str.index("m");
if occurance >=0:
    print ("'m' is found in the string and its index is: ", occurance);
else:
    print("'m' is not found in the string");