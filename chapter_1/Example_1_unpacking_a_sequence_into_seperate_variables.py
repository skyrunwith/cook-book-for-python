#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Problem
    You have an N-element tuple or sequence that you would like to unpack into a collection
    of N variables.
Solution
    Any sequence(or iterable) can be unpacked into variables using a simple assignment operation.
    The only requirement is that the number of variables and structure match the sequence.
Discussion
    Unpacking actually works with any object that happens to be iterable, not just tuples or lists.
    This includes strings, files, iterators, and generators.
    When unpacking, you may sometimes want to discard certain value. just pick a throwaway variable name for it.
"""

__author__ = 'Frankie Fu'
p = (4, 5)
x, y = p
print(x)
print(y)

data = ['ACME', 50, 91.1, (2012, 12, 21)]
name, shares, price, date = data
print(name, shares, price, date)

name, shares, price, (year, month, day) = data
print(name, shares, price, year, month, day)

# If there is a mismatch in the number of elements, you'll get an error.
p = (4, 5)
# x, y, z = p
# ValueError: not enough values to unpack (expected 3, got 2)

# Discussion
# strings
s = 'Hello'
a, b, c, d, e = s
print(a, b, c, d, e)
# discard certain values
data = ['ACME', 50, 90.1, (2021, 12, 31)]
_, shares, price, _ = data
print(shares, price)
