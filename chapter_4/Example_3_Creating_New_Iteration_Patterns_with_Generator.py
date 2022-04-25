#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Problem
    You want to implement a custom iteration pattern that's different than usual
    builtin functions(eg. range(), reversed(), etc.).
Solution
    1. using a generator function.
Discussion
    1. mere presence of the yield statement in a function turns it into a generator.
    2. a generator only runs in response to iteration.
    3. the key feature is that a generator function only run in response to "next" operations carried out in iteration.
"""

__author__ = 'Frankie Fu'


# Solution
def frange(start, stop, increment):
    """ generator function """
    x = start
    while x < stop:
        yield x
        x += increment


for n in frange(0, 10, 2):
    print(n)
print(list(frange(0, 1, 0.125)))


# Discussion
def countdown(n):
    print("Starting to count from", n)
    while n > 0:
        yield n
        n -= 1
    print("Done!")


c = countdown(3)
next(c)
next(c)
next(c)
next(c)
