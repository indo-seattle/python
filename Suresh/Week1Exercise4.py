#Write Python program that takes “I am living in Washintgon” and find “living” in the string using String find function.
str = input("Enter a string: ");
value = str.find("living");
if value >=0:
    print ("living index value is: ", value)
else:
    print ("Word 'living' is not in the entered string")
