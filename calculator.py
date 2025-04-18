"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""

import math

def add(a, b):
    a + b

def subtract(a, b):
    a - b

def multiply(a, b):
    a * b

def divide(a, b):
    b / a   # raise ZeroDivisionError if a == 0

def logarithm(a, b):
    math.log(b, a)# use math library/raise ValueError

def exponent(a, b):
    math.pow(a,b)


print("hi")

