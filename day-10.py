#day-10 of my python
'''
built-function
--------------
print()
input()
len()
type()
max()
min()
recursive functoin
------------------
--> a recursive function that calls it self to solve a program by breaking it
into small and simple sub-problem


def fac(num):
    if num == 1:
        return 1
    return num * fac(num -1)
print(fac(5))


def factorial(n):
    fact = 1

    for i in range(1, n + 1):
        fact = fact * i

    return fact

print(factorial(8))



def even(num):
    if num % 2 == 0:
        print("even")
    else:
        print("odd")
even(7)        

return
-------
-->this ends function execution and send a value back to the code that called the
function
eg:
--
def add(a,b):
    return a+b
res = add(4,5)
print(res)


lambda function
---------------
--> A lambda function is a small anonamus functions
-->lambda can take n number of arguments, but only one expression
syntax-->lambda arguments : expression

so = lambda a,b,c: a+b+c+a
print(so(3,4,9))


so = lambda a,b,c: a+b*c-a
print(so(3,4,9))

'''
def fac(num):
    if num == 1:
        return 1
    return num * fac(num -1)
print(fac(5))


def factorial(n):
    fact = 1

    for i in range(1, n + 1):
        fact = fact * i

    return fact

print(factorial(7))





















