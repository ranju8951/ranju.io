def fib(n):
    if n <= 0:
        return "n sholud be always positive"
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)
n=int(input("enter n value:"))
print(fib(n))
