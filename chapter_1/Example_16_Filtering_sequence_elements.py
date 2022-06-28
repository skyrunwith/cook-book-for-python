#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""" 
Problem
    You have data inside of a sequence, and need to extract values or reduce the sequence
    using some criteria.
Solution
    list comprehension. generator.
        the easiest and most straightforward ways to filter simple data.
    generator().
    filter() function.
        exception handling or some other complicate details.
Discussion
    list comprehension.
        could replace the not meet criteria value.
    filter function.
    itertools.compress()
        picks out the items corresponding to True values.
"""

__author__ = 'Frankie Fu'

# The easiest way to filter sequence data is often to use a list comprehension.
mylist = [1, 4, -5, 10, -7, 2, 3, -1]
print('n > 0: ', [n for n in mylist if n > 0])
print('n < 0: ', [n for n in mylist if n < 0])

# One Potential downside of using a list comprehension is that it might produce a large
# result if the original input is large. If this is a concern, you can use generator expressions
# to produce the filter values iteratively.
pos = (n for n in mylist if n > 0)
print(pos)

for x in pos:
    print(x)

# Sometimes, the filtering criteria cannot be easily expressed in a list comprehension or generator expression.
# For example, suppose that the filtering process involves exception handling or some other
# complicated detail. For this , put the filtering code into its own function and use
# built-in filter function.
values = ['1', '2', '-3', '-', '4', 'N/A', '5']


def is_int(val):
    try:
        x = int(val)
        return True
    except ValueError:
        return False


ivals = list(filter(is_int, values))
print(ivals)
# filter() creates an iterator, so if you want to create a list of results, make sure you
# also use list() as shown.


# Discussion
# List comprehension and generator also have the added power to transform the data
# at the same time.
mylist = [1, 4, -5, 10, -7, 2, 3, -1]
import math

print([math.sqrt(n) for n in mylist if n > 0])

# One variation on filtering involves replacing the values that don't meet the criteria with a new
# value instead of discarding them.
# For example, perhaps instead of just finding positive values, you want to also clip bad values to
# fit within a specified range. This is often easily accomplished by moving the filter criterion into
# a conditional expression like this:
clip_neg = [n if n > 0 else 0 for n in mylist]
print('replacing: ', clip_neg)
clip_pos = [n if n < 0 else 0 for n in mylist]
print('replacing: ', clip_pos)

# Another notable filtering tool is "itertools.compress()", which takes an iterable and an accompanying
# Boolean selector sequence as input. As output, it gives you all of the items in the iterable where
# the corresponding element in the selector is "Ture". This can be useful if you're trying to apply the
# results of filtering one sequence to another related sequence.
# For example, suppose you have the following two columns of data:
addresses = [
 '5412 N CLARK',
 '5148 N CLARK',
 '5800 E 58TH',
 '2122 N CLARK'
 '5645 N RAVENSWOOD',
 '1060 W ADDISON',
 '4801 N BROADWAY',
 '1039 W GRANVILLE',
]
counts = [0, 3, 10, 4, 1, 7, 6, 1]
# Now suppose you want to make a list of all addresses where the corresponding count value was greater than 5.
from itertools import compress

more5 = [n > 5 for n in counts]

print("more5: ", more5)

print(list(compress(addresses, more5)))
# The key here is to first create a sequence of Booleans taht indicates which elements
# satisfy the desired condition. The "compress()" function then picks out the items corresponding
# to "True" values.
