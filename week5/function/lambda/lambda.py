from functools import reduce
from tkinter import Y
def odd(n):
    return n%2==0

victor =[9, 45, 847, 9674, 42730]
weodd = filter(odd, victor)
weodd = list(weodd)
print (weodd)

def mult(x,y):
    return x*y

reducecharley = reduce(mult, victor)
print(reducecharley)

def wiskey(a, b, c):
    return a*b*c
print(wiskey(12,24,36))

def wiskey(*total):
    results = 1
    for i in total:
        results *= i
    return results
