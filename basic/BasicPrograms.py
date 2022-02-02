def factorial(n):
    return 1 if (n == 0 or n == 1) else n * factorial(n - 1)


# print(factorial(5))


# Another method to find the factorial
def fact(n):
    if n < 0:
        return 0
    elif n == 0 or n == 1:
        return 1
    else:
        f = 1
        while n > 1:
            f *= n
            n -= 1
        return f


# print('Another method to find the factorial. Factorial of {} is {}'.format(5, fact(5)))
