#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Searching and Replacing Text
Problem
    You want to search for and replace a text pattern in a string.
Solution
    use the "str.replace()" method.

    sub() functions/methods in re method.

    subn()
Discussion
    There isn't much more to regular expression search and replace than the sub() method shown.
    The trickiest part is specifying the regular expression pattern -- something that's best
    left as an exercise to the reader.
"""

__author__ = 'Frankie Fu'

# Solution
# For simple literal pattern, use the str.replace() method. For example:
text = 'yeah, but no, but yeah, but no, but yeah'

print(text.replace('yeah', 'yep'))

# For more complicated patterns, use the "sub()" functions/methods in the "re module".
# To illustrate, suppose you want to rewrite dates if the form '11/27/2012' as '2012-11-27'
# Here is a sample of how to do it:
text = 'Today is 11/27/2012. PyCon starts 3/13/2013.'
import re

print(re.sub(r'(\d+)/(\d+)/(\d+)', r'\3-\1-\2', text))
# Today is 2012-11-27. PyCon starts 2013-3-13.

# The first argument to "sub()" is the pattern to match and the second argument is the
# replacement pattern. Backslashed digits such as "\3" refer to capture group numbers in the pattern.

# If you're going to perform repeated substitutions of the same pattern, consider compiling it first for
# better performance. For example:
import re

datepat = re.compile(r'(\d+)/(\d+)/(\d+)')
print(datepat.sub(r'\3-\1-\2', text))
# Today is 2012-11-27. PyCon starts 2013-3-13.

# For more complicated substitutions, it's possible to specify a substitution callback function instead.
# For example:
from calendar import month_abbr


def change_date(m):
    mon_name = month_abbr[int(m.group(1))]
    return f'{m.group(2)} {mon_name} {m.group(3)}'


print(datepat.sub(change_date, text))
# Today is 27 Nov 2012. PyCon starts 13 Mar 2013.

# As input, the argument to the substitution callback is a match object, as returned by "match()" or "find()".
# Use the ".group()" method to extract specific parts of the match. The function should return the replacement text.

# If you want to know how many substitutions wre made in addition to getting the replacement text, use "re.subn()"
# instead. For example:
newtext, n = datepat.subn(r'\3-\1-\2', text)
print(newtext)
# Today is 2012-11-27. PyCon starts 2013-3-13.
print(n)
# 2


