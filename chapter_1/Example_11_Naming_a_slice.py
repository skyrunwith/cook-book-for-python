#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""" 
Problem
    Your program has become an unreadable mess o f hardcode slice indices and you want to clean it up.
Solution
    name the slices.
        SHARES = slice(20, 23)
Discussion
    indices(size) method
"""

__author__ = 'Frankie Fu'

# Suppose you have some code that is pulling specific data fields out of a record string
# with fixed fields(e.g, from a flat file or similar format)
record = '....................100.................513.25 ..........'
cost = int(record[20:23]) * float(record[40:46])
print(cost)

# Instead of doing that, why not name the slices like this?
SHARES = slice(20, 23)
PRICE = slice(40, 46)
cost = int(record[SHARES]) * float(record[PRICE])
print(cost)

# Discussion
# In general, the built-in slice() creates a slice object that can be used anywhere a slice is allowed.
items = [0, 1, 2, 3, 4, 5, 6]
a = slice(2, 4)
print(items[2:4])

print(items[a])

items[a] = [10, 11]
print(items)

del items[a]

print(items)

# If you have slice instance s, you can get more information about it by looking at its
# s.start, s.stop, and s.step attributes, respectively.
a = slice(10, 50, 2)
print(a.start, a.stop, a.step)

# In addition, you can map a slice onto a sequence of a specific size by using its indices(size)
# method. This returns a tuple (start, stop, step) where all values have been suitably limited
# to fit within bounds(as to avoid IndexError Exceptions when indexing).
a = slice(5, 10, 2)
s = 'HelloWorld'
print(a.indices(len(s)))

for i in range(*a.indices(len(s))):
    print(s[i])