def lcm(x, y):

    # choose the greater number
    if x > y:
        greater = x
    else:
        greater = y
    while(True):
        if((greater % x == 0) and (greater % y == 0)):
            lcm = greater
            break
        greater += 1
    return lcm

def gcd(x, y):
    while(y):
        x, y = y, x % y
    return x

def hcf(x, y):

    # choose the smaller number
    if x > y:
        smaller = y
    else:
        smaller = x
    for i in range(1, smaller+1):
        if((x % i == 0) and (y % i == 0)):
            hcf = i
    return hcf


num1 = 12
num2 = 14


print("The L.C.M. of", num1,"and", num2,"is", lcm(num1, num2))
print("The G.C.D. of", num1,"and", num2,"is", gcd(num1, num2))
print("The H.C.F. of", num1,"and", num2,"is", hcf(num1, num2))