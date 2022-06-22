#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""" 
Problem
    You want to eliminate the duplicate values in a sequence, but preserve the order of the remaining items.
Solution
    hashable or unhashable.
        using a set and a generator.
Discussion
    why not use set?
        because, it doesn't preserve ordering.
"""

__author__ = 'Frankie Fu'


# If the values in the sequence are hashable, the problem can be easily solved using a set
# and a generator. For example:
def dedupe(items):
    seen = set()
    for item in items:
        if item not in seen:
            yield item
            seen.add(item)


# Here is an example of how to use your function:
a = [1, 5, 2, 1, 9, 1, 5, 10]
print(list(dedupe(a)))


# If you are trying to eliminate duplicates in a sequence of unhashable types(such as dicts),
# you can make a slight change to this recipe, as follows:
def dedupe(items, key=None):
    seen = set()
    for item in items:
        val = item if key is None else key(item)
        if val not in seen:
            yield item
            seen.add(val)


# Here, the suppose of the key argument is to specify a function that converts sequence
# items into a hashable type for the purpose of duplicate detection. Here's how it works:
a = [{'x': 1, 'y': 2}, {'x': 1, 'y': 3}, {'x': 1, 'y': 2}, {'x': 2, 'y': 4}]
print(list(dedupe(a, key=lambda d: (d['x'], d['y']))))


# Discussion
# If all you want to do is eliminate duplicate, it is often easy enough to make a set.
a = [1, 5, 2, 1, 9, 1, 5, 10]
print(set(a))
# However, it doesn't preserve any kind of ordering.
