#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""" 
Problem
    You have two dictionaries and want to find out what they might have in common(same, keys,
    some values, etc.).
Solution
    keys(): keys-view object
        feature: common set operations such as union, intersection and difference.
    items(): (key-value) pairs.
        used to perform operations such as finding out which key-value pairs two dictionaries have in common.
    values(): not support set operations.
        the items contained in a values view aren't guaranteed to be unique.
Discussion
"""

__author__ = 'Frankie Fu'

# Consider two dictionaries
a = {
    'x': 1,
    "y": 2,
    "z": 3
}

b = {
    'w': 10,
    'x': 11,
    'y': 2
}

# To find out what the two dictionaries have in common, simply perform common set
# operations using keys() or items() method. For example;
# Find keys in common
print(a.keys() & b.keys())  # {'x', 'y'}

# Find keys in a that are not in b
print(a.keys() - b.keys())  # {'z'}

# Find (key, value) pairs in common
print(a.items() & b.items())  # {('y', 2)}

# These kinds of operations can also be used to alter or filter dictionary content. For
# example, suppose you want to make a new dictionary with selected keys removed. Here
# is some sample code using a dictionary comprehension:

# Make a new dictionary with certain keys removed
c = {key: a[key] for key in a.keys() - {'z', 'w'}}
print(c)  # {'x': 1, 'y': 2}
