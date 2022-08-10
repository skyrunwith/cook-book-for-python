#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Rounding Numerical Values
Problem
    You want to round a floating-point number to a fixed number of decimal places.
Solution
    Use the built-in "round(value, ndigits)" functions.
Discussion
    Don't confuse rounding with formatting a value for output. If your goal is simply to output a numerical
    value with certain number of decimal places, you don't typically need to use round(). Instead, just specify the
    desired precision when formatting.
    For financial, suggest use 'decimal' module.
"""

__author__ = 'Frankie Fu'

# Solution
# For simple rounding, use the built-in round(value, ndigits) function. For example:
print(round(1.23, 1))
# 1.2
print(round(1.27, 1))
# 1.3
print(round(-1.27, 1))
# -1.3
print(round(1.25361, 3))
# 1.254

# When a value is exactly halfway between two choices, the behavior of round is to round to the nearest even digit.
# That is, values such as 1.5 or 2.5 both get rounded to 2. The number of digits given to round() can be  negative
# in which case rounding take place of tens, hundreds, thousands, and so on. For example:
a = 1627731
print(round(a, -1))
# 1627730

print(round(a, -2))
# 1627700

print(round(a, -3))
# 1628000

# Discussion
# Don't confuse rounding with formatting a value for output. If your goal is simply to output a numerical
# value with certain number of decimal places, you don't typically need to use round(). Instead, just specify the
# desired precision when formatting. For example:
x = 1.23456
print(format(x, '0.2f'))
# 1.23
print(format(x, '0.3f'))
# 1.235
print('value is {:0.3f}'.format(x))
# value is 1.235
# Also, resist urge to round floating-point numbers to "fix" perceived accuracy problems. For example, you might be
# inclined to do this:
a = 2.1
b = 4.2
c = a + b
print(c)

c = round(c, 2)  # "Fix" result()
print(c)
# 6.3

# For most applications involving floating point, it simply not necessary(or recommended) to do this. Although there
# are small errors introduced into calculations, the behavior of those errors are understood and tolerated. If avoiding
# such errors is important (e.g, in financial applications, perhaps), consider the use of "decimal" module, which
# is discussed in the next recipe.





















