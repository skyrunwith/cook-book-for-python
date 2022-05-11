#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Problem
    You would like to define a generator function, but it involves extra state that you
    would like to expose to the user somehow.
Solution
    You can easily implement it as a class, putting the generator function code in the
    __iter__() method.
    Since it creates an instance, You can access internal attributes.
Discussion
    With generators, it is easy to fall into a trap of trying to do everything with functions
    alone. This can lead to rather complicated code if the generator function needs to interact
    with other parts of your program in unusual ways(exposing attributes, allowing control via method calls, etc.)
    # 解决方案
    Defining your generator in the __iter__() method.
    # Note that
    It might require an extra step of calling iter() if you are going to drive iteration
    using a technique other than a for loop.
"""

__author__ = 'Frankie Fu'

# Solution
from collections import deque


class linehistory:
    def __init__(self, lines, histlen=3):
        self.lines = lines
        self.history = deque(maxlen=histlen)

    def __iter__(self):
        for lineno, line in enumerate(self.lines, 1):
            self.history.append((lineno, line))
            yield line

    def clear(self):
        self.history.clear()


with open('./data/somefile.txt') as f:
    lines = linehistory(f)
    for line in lines:
        if 'python' in line:
            for lineno, hline in lines.history:  # access internal attributes.
                print('{}:{}'.format(lineno, hline), end='')


# Discussion
f = open('./data/somefile.txt')
lines = linehistory(f)
# TypeError: 'linehistory' object is not an iterator
# next(lines)

# Call iter() first, then start iterating
it = iter(lines)
print(next(it))
print(next(it))
