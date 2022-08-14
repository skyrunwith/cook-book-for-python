"""
Calculating with Fractions
Problem
    You have entered a time machine and suddenly find yourself working on elementary-level homework problems
    involving fractions. Or perhaps you're writing code to make calculations involving measurements made
    in your wood shop.
Solution
    The 'fractions' module can be used to perform mathematical calculations involving fractions.
Discussion
"""

__author__ = 'Frankie Fu'

# Solution
from fractions import Fraction

a = Fraction(5, 4)
b = Fraction(7, 16)
print(a + b)
# 27/16
print(a * b)
# 35/64

# Getting numerator/dominator
c = a * b
print(c.numerator, c.denominator)
# 35 64
# Converting to a float
print(float(c))
# 0.546875
# Limiting the denominator of a value
print(c.limit_denominator(8))
# 4/7
# Converting a float to a fraction
x = 3.75
y = Fraction(*x.as_integer_ratio())
print(y)
# 15/4

# Calculating with fractions doesn't arise often in most programs, but there are situations where it might
# make sense to use them. For example, allowing a program to accept units of measurement in fractions and
# performing calculations with them in that form might alleviate the need for a user to manually make
# conversions to decimals or floats.



