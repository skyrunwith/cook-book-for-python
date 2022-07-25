#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Aligning Text Strings
Problem
    You need to format text with some sort of alignment applied.
Solution
    For basic alignment of strings, the 'ljust()', 'rjust()', and 'center()' methods of strings
    can be used. For example:
Discussion
    format is more general purpose than using ljust(), rjust(), or center() method of strings in
    that it works with any kind of object.
"""

__author__ = 'Frankie Fu'

# Solution
text = 'Hello World'
print(text.ljust(20))

print(text.rjust(20))

print(text.center(20))

# Hello World
#          Hello World
#     Hello World

# All of these methods accept an optional fill character as well. For example:
print(text.rjust(20, '='))

print(text.center(20, '*'))

# The format() function can also be used to easily align things. All you need to do is use
# the '<, >, or ^' characters along with a desired width. For example:
print(format(text, '>20'))

print(format(text, '<20'))

print(format(text, '^20'))
#          Hello World
# Hello World
#     Hello World

# If you want to include a fill character other than a space, specify it before the alignment character:
print(format(text, '=>20s'))
# =========Hello World
print(format(text, '*^20'))
# ****Hello World*****

# These format codes can also be used in the 'format()' method when formatting multiple values.
# For example:
print('{:>10s} {:>10s}'.format('Hello', 'World'))
#      Hello      World

# One benefit of 'format()' is that it is not specific to strings. It works with any value, making it
# more general purpose. For instance, you can use it with numbers:
x = 1.2345
print(format(x, '>10'))
#     1.2345
print(format(x, '^10.2f'))
# '   1.23   '

# Discussion
# In older code, you will also see the % operator used tot format text. For example:
'''
'%-20s' % text
# 'Hello World     '
'%20s' % text
'       Hello World'
'''

# However, in new code, you should probably prefer the use of the format() function or method. format()
# is a lot more powerful than what is provided with the % operator. Moreover, format() is more general
# purpose than using the 'ljust(), rjust(), or center()' method of strings in that it works with any
# kind of object.

# For a complete list of feature available with the format() function. consult the
# online Python documentation.(http://docs.python.org/3/library/string.html#formatspec)
