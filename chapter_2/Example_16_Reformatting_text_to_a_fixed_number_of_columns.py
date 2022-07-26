#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Reformatting Text to a Fixed Number of Columns
Problem
    You have long strings that you want to reformat so that they fill a user-specified number of columns.
Solution
    Use the "textwrap" module to reformat for output.
Discussion
"""

__author__ = 'Frankie Fu'

# Solution
# For example, suppose you have the following long string:
s = "Look into my eyes, look into my eyes, the eyes," \
    "the eyes, not around the eyes, don't look around the eyes" \
    "look into my eyes, you're under."

# Here's how you can use the textwrap module reformat it in various ways:
import textwrap

print(textwrap.fill(s, 70))
'''
Look into my eyes, look into my eyes, the eyes,the eyes, not around
the eyes, don't look around the eyeslook into my eyes, you're under.
'''
print(textwrap.fill(s, 40))
'''
Look into my eyes, look into my eyes,
the eyes,the eyes, not around the eyes,
don't look around the eyeslook into my
eyes, you're under.
'''
print(textwrap.fill(s, 40, initial_indent='    '))
'''
    Look into my eyes, look into my
eyes, the eyes,the eyes, not around the
eyes, don't look around the eyeslook
into my eyes, you're under.
'''

print(textwrap.fill(s, 40, subsequent_indent='    '))
'''
    the eyes,the eyes, not around the
    eyes, don't look around the eyeslook
    into my eyes, you're under.
'''

# Discussion
# The 'textwrap' module is a straightforward way to clean up text for printing--especially
# if you want the output to fit nicely on the terminal. On the subject of the terminal size,
# you can obtain it using 'os.get_terminal_size()'. For example:
import os

# print(os.get_terminal_size())

# The fill() method has a few additional options that control how handles tabs, sentence endings,
# and so on. Look at the documentation for the textwrap.TextWrapper class for further details.
# http://docs.python.org/3.3/library/textwrap.html#textwrap.TextWrapper
