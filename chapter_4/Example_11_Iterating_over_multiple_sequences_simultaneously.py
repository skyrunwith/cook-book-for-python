#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Problem
    You want to iterate over the items contained in more than one sequence at a time.
Solution
    use the zip() function, iterate over more than one sequence simultaneously.
Discussion
    dict(zip())
    list(zip())
    zip_longest()
    zip() return an iterator as result.
"""

__author__ = 'Frankie Fu'

# Solution
xpts = [1, 5, 4, 2, 10, 7]
ypts = [101, 78, 37, 15, 62, 99]
# zip(a, b) produces tuples (x, y)
for x, y in zip(xpts, ypts):
    print(x, y)

# the length of the iteration is the same as the length of the shortest input.
a = [1, 2, 3]
b = ['w', 'x', 'y', 'z']
for i in zip(a, b):
    print(i)
'''
(1, 'w')
(2, 'x')
(3, 'y')
'''

# use itertools.zip_longest().
from itertools import zip_longest
for i in zip_longest(a, b):
    print(i)
'''
(1, 'w')
(2, 'x')
(3, 'y')
(None, 'z')
'''

for i in zip_longest(a, b, fillvalue=0):
    print(i)
'''
(1, 'w')
(2, 'x')
(3, 'y')
(0, 'z')
'''

# Discussion
# 1.zip() is commonly used whenever you need to pair data together.
# for example, headers and columns
headers = ['name', 'shares', 'price']
columns = ['ACME', 100, 400.1]
s = dict(zip(headers, columns))
print(s)

# Alternatively, if you are trying to produce output.
for name, val in zip(headers, columns):
    print(name, '=', val)

# 2.It's less common, but zip() can be passed more than two sequences as input.
a = [1, 2, 3]
b = [10, 11, 12]
c = ['x', 'y', 'z']
for i in zip(a, b, c):
    print(i)

# Last but not least, it's important to emphasize that zip() creates an iterator as a result.
# If you need the paired values stored in a list, use the list function.
print(zip(a, b))
print(list(zip(a, b)))