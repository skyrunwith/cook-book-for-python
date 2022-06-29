#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""" 
Problem
    You have multiple dictionaries or mappings that you want to logically combine into
    single mapping to perform certain operations, such as looking up values or checking
    for the existence of keys.
Solution
    collections.ChainMap.
        A ChainMap takes multiple mappings and makes them logically appear as one.
        It simply keeps a list of the underlying mappings and redefines common dictionary operations to scan this list.
Discussion
"""

__author__ = 'Frankie Fu'

# Solution
# Suppose you have two dictionaries
a = {'x': 1, 'z': 3}
b = {'y': 2, 'z': 4}

# Now suppose you want to perform lookups where you have to check both dictionaries
# (e.g, first checking in a and then in b if not found). Any easy way to do this is
# to use the "ChainMap" class from the collections module.
from collections import ChainMap

c = ChainMap(a, b)
print('ChainMap(a, b): ', c)
print(c['x'])  # 1 (from a)
print(c['y'])  # 2 (from b)
print(c['z'])  # 3 (from a)

# Discussion
# A ChainMap takes multiple mappings and makes them logically appear as one. However,
# the mappings are not literally merged together. Instead, a ChainMap simply keeps a list
# of the underlying mappings and redefines common dictionary operations to scan the list.
# Most operations will work. For Example
print('len(c): ', len(c))

print("list(c.keys()): ", list(c.keys()))

print("list(c.values()): ", list(c.values()))

# If there are duplicate keys, the values from the first mapping get used. Thus, the entry
# c['z'] in the example would always refer to the values in dictionary a, not the value in
# dictionary b.

# Operations that mutate the mapping always affect the first mapping listed.
c['z'] = 10
c['w'] = 40

del c['x']
print(a)

















