#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Combining and Concatenating Strings
Problem
    You want to combine many small strings together into a large string.
Solution
    If the strings you wish to combine are found in a sequence or iterable, the fastest way to
    combine them is to use the 'join()' method.

    If you're only combining a few strings, using '+' usually works well enough.

    If you're trying to combine string literal together in source code, you can simply place
    them adjacent to each other with no '+' operator.
        a = 'Hello' 'World'
Discussion
    Performance:
    + operator, will create a new temporary string object.

    Mixing I/O operations and string concatenation.

    if you're writing coed that is building output from lots of small strings, you might
    consider writing that code as a generator function, using yield to emit fragments.
"""

__author__ = 'Frankie Fu'

# Solution
# For example
parts = ['Is', 'Chicago', 'Not', 'Chicago?']
print(' '.join(parts))
# Is Chicago Not Chicago?
print(','.join(parts))
# Is,Chicago,Not,Chicago?
print(''.join(parts))
# IsChicagoNotChicago?

# At first glance, this syntax might look really odd, but the join() operation is specified as a method
# on strings. Partly this is because the objects you want to join could come from any number of different
# data sequences(e.g, lists, tuples, dicts, files, sets, or generators), and it would be redundant to have
# join() implemented as a method on all of those objects separately. So you just specify the separator
# string that you want and use the join() method on it to glue text fragment together.

# If you're only combining a few strings, using + usually works well enough:
a = 'Is Chicago'
b = 'Not Chicago?'
print(a + ' ' + b)
# Is Chicago Not Chicago?

# The + operator also works fine as a substitute for more complicated string formatting operations.
# For example:
print('{} {}'.format(a, b))
# Is Chicago Not Chicago?
print('a' + ' ' + b)
# a Not Chicago?

# If you're trying to combine string literals together in source code, you can simply place them
# adjacent to each other with no + operator. For example:
a = 'Hello' 'World'
print(a)
# HelloWorld

# Discussion
# Joining string together might not seem advanced enough to warrant an entire recipe, but it's often
# an area where programmers make programming choices that severely impact the performance of their code.

# The most important thing to know is that using the + operator to join a lot of strings together is
# grossly inefficient due to the memory copies and garbage collection that occurs. In particular, you
# never want to write code that joins strings together like this:
s = ''
for p in parts:
    s += p

# This runs quite a bit slower than using the join() method, mainly because each += operation creates
# a new string object. You're better off just collecting all of the parts first and then joining them
# together at the end.

# One related(and pretty neat) trick is the conversion of data to strings and concatenation at
# the same time using a generator expression, as described in Recipe 1.10. For example:
data = ['ACME', 50, 91.1]
print(','.join(str(d) for d in data))
# ACME,50,91.1

# Also be on the lookout for unnecessary string concatenations. Sometimes programmers get carried away
# with concatenation when it's really not technically necessary. For example, when printing:
a, b, c = 'a', 'b', 'c'
print(a + ':' + b + ':' + c)  # Ugly

print(':'.join([a, b, c]))  # Still ugly

print(a, b, c, sep=":")  # Better

# Mixing I/O operations and string concatenation is something that might require study in your application.
# For example, consider the following two code fragments:
# Version1 (string concatenation)
'''
f.write(chunk1 + chunk2)
'''

# Version2 (separate I/O operations)
'''
f.write(chunk1)
f.write(chunk2)
'''


# If the two strings are small, the first version might offer much better performance due to the inherit
# expense of carrying out an I/O system call. On the other hand, if the two strings are large, the second
# version may be more efficient, since it avoids making a large temporary result and copying large blocks
# of memory around. Again, it must be stressed that this is something you would have to study in relation
# to your own data in order to determine which performs best.

# Last, but not least, if you're writing code that is building output from lots of small strings, you
# might consider writing that code as a generator function, using 'yield' to emit fragments.
# For example:
def sample():
    yield 'Is'
    yield 'Chicago'
    yield 'Not'
    yield 'Chicago?'


# the interesting thing about this approach is that it makes no assumption about how the fragments
# are to be assembled together. For example, you could simply join the fragments using join():
text = ''.join(sample())

# Or you could redirect the fragments to I/O:
'''
for part in sample():
    f.write(part)
'''


# Or you could come up with some kind of hybird scheme that's smart about combing I/O operations:
def combine(source, maxsize):
    parts2 = []
    size = 0
    for part in source:
        parts2.append(part)
        size += len(part)
        if size > maxsize:
            yield ''.join(parts2)
            parts2 = []
            size = 0
    yield ''.join(parts2)

# The key point is that the original generator function doesn't have to know the precise details.
# It just yield the parts.