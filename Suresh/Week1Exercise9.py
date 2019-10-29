#Write Python program that takes “zerorez” and revese the string, and then compres with the original and print True if they both are same.
str = input("Enter a string: ");
revstr = '';
for i in str:
    revstr=i+revstr;
print(revstr);

if str == revstr:
    print("Entered string is a palindrome")
else:
    print("Entered string is not a palindrome")
