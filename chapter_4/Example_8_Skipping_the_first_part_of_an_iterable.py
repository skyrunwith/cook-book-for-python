#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Problem
    You want to iterate over items in an iterable, but the first few items aren't of interest and you just
    want to discard them.
Solution
    itertools.dropwhile() function. To use it, you supply a function and an iterable. The returned iterator discards
    the first items in the sequence as long as the supplied function return True. Afterward, the entirely of the sequence
    is produced.

    itertools.islice() function.
Discussion
    this recipe works with all iterables, including generators, files, and similar kinds of object.

    It's different than simply filtering all of it.
"""

__author__ = 'Frankie Fu'

# Solution
with open('data/somefile.txt') as f:
    for line in f:
        print(line, end='')

# Skipping the first items according to a test function.
from itertools import dropwhile
print('\n\ndropwile:>>>')
with open('data/somefile.txt') as f:
    for line in dropwhile(lambda line: line.startswith('j'), f):
        print(line, end='')


# If you happen to know the exact number of items you want to skip.
# a slice of [3:]
from itertools import islice
print('\n\nislice:>>>')
items = ['a', 'b', 'c', 1, 4, 10, 15]
for x in islice(items, 3, None):
    print(x)


# Discussion
# Messy code
print('\n\nMessy code:>>>')
with open('data/somefile.txt') as f:
    # Skip over initial comments
    while True:
        line = next(f, '')
        if not line.startswith("j"):
            break

    # Process remaining lines
    while line:
        # Replace with useful processing
        print(line, end='')
        line = next(f, None)

# Filtering all of it
# 过滤掉所有的，而不是只过滤开始的部分。
print("\n\nFiltering all:>>>")
with open('data/somefile.txt') as f:
    lines = (line for line in f if not line.startswith("j"))
    for line in lines:
        print(line, end='')
