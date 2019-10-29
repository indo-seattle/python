#Write Python program that takes “123456” and print True if all the characters in the text are numeric using string isnumeric function.
input = input("Enter a value: ")
if input.isnumeric():
    print("Entered Value is a number")
else:
    print("Entered value is not a number");