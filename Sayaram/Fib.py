def fib(n):
    a, b, lp = 0, 1, 1
    while lp < n:
        a, b = b, a+b
        lp +=1
    return a

print(fib(10))



def recur_fibo(n):
    if n <= 1:
        return n
    else:
        return(recur_fibo(n-1) + recur_fibo(n-2))

print(recur_fibo(10))