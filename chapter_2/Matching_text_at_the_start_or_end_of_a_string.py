"""
Matching Text at the start_or_end_of_a_string
Problem
    You need to check the start or end of a string for specific text patterns, such as filename
    extensions, URI schemas, and so on.
Solution
    str.startswith() and str.endswith() methods.
Discussion
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
print(filenames)
a = [name for name in filenames if name.endswith(('.py'))]
print(a)

b = any(name.endswith('.py') for name in filenames)
print(b)