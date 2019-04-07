print("Exercise B7 - Python factorial")

# Python program to find the factorial of a number using recursion

def factorialFunction(n):
   if n == 1:
       return n
   else:
       return n*factorialFunction(n-1)

x = int(input("Enter a number: "))

y = factorialFunction(x)

print('Factoarial of ', x , 'is : ', y)