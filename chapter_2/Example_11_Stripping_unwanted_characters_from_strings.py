#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Stripping Unwanted Characters from Strings
Problem
    You want to strip unwanted characters, such as whitespace, from the beginning, end, or middle
    if a text string.
Solution
    beginning, end:
        strip()
        lstrip()
        rstrip()
Discussion
    The various strip() methods are commonly used when reading and cleaning up data for later
    processing. For example, you can use them to get rid of whitespace, remove quotations, and
    other tasks.

    inner space: replace(), re.sub()

    a generator expression can be useful, when iteratively prcessing.
"""

__author__ = 'Frankie Fu'

# Solution
# The 'strip()' method can be used to strip characters from the beginning or end of a string.
# 'lstrip()' and 'rstrip()' perform stripping from the left or right side, respectively. By
# default, these methods strip whitespace, but other characters can be given. For example:

# Whitespace stripping
s = '   hello world  \n'
print(s.strip())
'hello world'
print(s.lstrip())
'hello world  \n'
print(s.rstrip())
'   hello world'

# Character stripping
t = '-----hello====='
print(t.lstrip('-'))
'hello====='
print(t.strip('-='))
'hello'

# Discussion
# The various strip() methods are commonly used when reading and cleaning up data for later processing.
# For example, you can use them to get rid of whitespace, remove quotations, and other tasks.

# Be aware that stripping does not apply to any text in the middle of a string. For example:
s = '   hello       world   \n'
s = s.strip()
print(s)
'hello       world'

# If you needed to do something to the inner space, you would need to use another technique, such as
# using the replace method or a regular expression substitution. For example:
print(s.replace(' ', ''))
'helloworld'

import re

print(re.sub(r'\s+', ' ', s))
# hello world

# It is often the case that you want to combine string stripping operations with some other kind of
# iterative processing, such as reading lines of data from a file. If so, this is one area where
# a generator expression can be useful. For example:
'''
with open(filename) as f:
    lines = (line.strip() for line in f)
    for line in lines:
        ...
'''
# Here, the expression lines = (line.strip() for line in f) acts as a kind of data transform. It's
# efficient because it doesn't actually read the data into any kind of temporary list first. It just
# creates an iterator where all of the lines produced have the stripping operation applied to them.

# For even more advanced stripping, you might turn to the 'translate()' method. See the next recipe
# on sanitizing strings for further details.






















