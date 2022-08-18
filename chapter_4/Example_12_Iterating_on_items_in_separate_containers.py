#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Problem
    You need to perform the same operation on many objects, but the objects are contained
    in different containers. and you'd like to avoid nested loops without losing readability
    of your code.
Solution
    itertools.chain(): It takes a list of iterable as input, adn returns an iterator that effectively masks
    the fact that you're really acting on multiple containers.
Discussion
    It's far more efficient with memory if the input sequences are large and it can be easily applied when
    the iterables in question are of different types.
"""

__author__ = 'Frankie Fu'

# Solution
from itertools import chain

a = [1, 2, 3, 4]
b = ['x', 'y', 'z']
for x in chain(a, b):
    print(x)
# 1
# 2
# 3
# 4
# x
# y
# z

# A common use of 'chain()' is in programmers where you would like to perform certain operations on all of
# the items at once but the items are pooled into different working sets. For example:
# Various working sets of items
active_items = set({1, 2, 3})
inactive_items = set({3, 4, 5, 5})

# Iterate over all items
for item in chain(active_items, inactive_items):
    # Process item
    print(item)
    # 1
    # 2
    # 3
    # 3
    # 4
    # 5

# This solution is much more elegant than using two separate loops, as in the following:
print('active items:')
for item in active_items:
    print(item)
# 1
# 2
# 3
print('inactive items:')
for item in inactive_items:
    print(item)
# 3
# 4
# 5

# Discussion
# itertools.chain() accepts one or more iterables as arguments. It then works by creating an iterator that successively
# consumes and returns the items produced by each of the supplied iterables you provided. It's a subtle distinction.
# but chain() is more efficient than first combining the sequences and iterating. For example:

"""
# Inefficient
for x in a + b:
    ...
# Better 
for x in chain(a, b):
    ...
"""

# In the first case, the operation a + b creates an entirely new sequence and additionally requires a and b to be of
# the same type. 'chain()' performs no such operations, so it's far more efficient with memory if the input sequences
# are large and it can be easily applied when the iterables in question are of different types.








