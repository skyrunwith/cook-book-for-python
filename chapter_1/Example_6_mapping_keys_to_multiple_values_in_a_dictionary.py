#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""" 
Problem
    You want to make a dictionary that maps keys to more than one value(a so-called "multidict")
Solution
    store the multiple values in another container such as a list or set.
    defaultdict.
Discussion
"""
__author__ = 'Frankie Fu'

# Solution
# store values in list or set
d = {
    'a': [1, 2, 3],
    'b': [4, 5]
}

e = {
    'a': {1, 2, 3},
    'b': {4, 5}
}

# To easily construct such dictionaries, you can use "defaultdict" in the collections
# module. A feature of defaultdict is that it automatically initializes the first value
# so you can simply focus on adding items.
from collections import defaultdict

d = defaultdict(list)
d['a'].append(1)
d['a'].append(2)
d['b'].append(4)

d = defaultdict(set)
d['a'].add(1)
d['a'].add(2)
d['b'].add(4)

# One caution with deafultdict is that it will automatically create dictionary entries for
# keys accessed later on(even if they aren't currently found in the dictionary). If you
# don't want this behavior, you might use setdefault() on an dictionary instead.
d = {}  # A regular dictionary
d.setdefault('a', []).append(1)
d.setdefault('a', []).append(2)
d.setdefault('b', []).append(4)
# However, many programmers find setdefault() to be a little unnatural.

# Discussion
# In principle, constructing a multivalued dictionary is simple. However, initialization of
# the first value can be messy if you try to do it yourself.
pairs = [('foo', 1), ('bar', 6)]
d = {}
for key, value in pairs:
    if key not in d:
        d[key] = []
    d[key].append(value)

print(d)

# Using a defaultdict simply leads to much cleaner code:
d = defaultdict(list)
for key, value in pairs:
    d[key].append(value)

print(d)

