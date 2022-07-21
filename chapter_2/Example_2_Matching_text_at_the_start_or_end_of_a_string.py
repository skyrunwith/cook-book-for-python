"""
Matching Text at the start_or_end_of_a_string
Problem
    You need to check the start or end of a string for specific text patterns, such as filename
    extensions, URI schemas, and so on.
Solution
    str.startswith() and str.endswith() methods.
Discussion
    Similar operations can be performed with slices, but are far less elegant.
        slices. [:5], [-4:]
    regular expression:
        re.match('http:|https:|ftp:', url)
    data reduction:
        if any(name.endswith(('.c', '.h')) for name in listdir(dirname)):
            ...
"""

__author__ = 'Frankie Fu'

# Solution
filename = 'spam.txt'
print(filename.endswith('.txt'))
print(filename.startswith('file:'))
url = 'http://www.ptyhon.org'
print(url.startswith('http:'))

# If you need to check against multiple choices, simply provide a tuple of possibilities to
# startswith() or endswith()
import os

filenames = os.listdir('.')
print('listdir:', filenames)
a = [name for name in filenames if name.endswith(('.py'))]
print(a)

b = any(name.endswith('.py') for name in filenames)
print(b)

# Here is another example:
from urllib.request import urlopen


def read_data(name):
    if name.startswith(('http:', 'https:', 'ftp:')):
        return urlopen(name).read()
    else:
        with open(name) as f:
            return f.read()


# Oddly, this is one part of Python where a tuple is actually required as input. If you happen to have
# the choices specified in a list or set, just make sure you convert them using tuple() first.
# For example:
choices = ['http:', 'ftp:']
url = 'http://www.python.org'
# print(url.startswith(choices))
# TypeError: startswith first arg must be str or a tuple of str, not list
print(url.startswith(tuple(choices)))

# Discussion
# The startswith() and endswith() methods provide a very convenient way to perform basic prefix
# and suffix checking. Similar operations can be performed with slices, but are far less elegant.
# For example:
filename = 'spam.txt'
print(filename[-4:] == '.txt')
# True
url = 'http://www.python.org'
print(url[:5] == 'http:' or url[:6] == 'https:' or url[:4] == 'ftp:')
# True

# You might also be inclined to use regular expressions as an alternative. For example:
import re

url = 'http://www.python.org'
print(re.match('http:|https:|fpt:', url))

# This works, but is often overkill for simple matching. Using this recipe is simpler and run faster:

# Last, but not least, the "startswith()" and "endswith()" methods look nice when combined with other
# operations, such as common data reductions. For example, this statement that checks a directory for
# the presence of certain kinds of files:
if any(name.endswith(('.c', '.h')) for name in os.listdir("dirname")):
    ...

































