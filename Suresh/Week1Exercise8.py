#Write Python program that takes “One day I buy one Tesla car” and print the number of times the value "one" appears in the string using string count function
str = input("Enter a string: ");
count = str.count("one");
if count >=1:
    print("Number of occurrence 'one' appeared: ", count);
else:
    print("There are no occurrences of 'one'");