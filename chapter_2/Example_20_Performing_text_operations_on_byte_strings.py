#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Performing text operations on byte strings
Problem
    You want to perform common text operations(e.g, stripping, searching, and replacement) on byte strings.
Solution
    Byte strings already support most of the same built-in operations as text strings.
Discussion
    If you're working with text, use normal text string in your program, not byte strings.
"""

__author__ = 'Frankie Fu'

# Solution
# Byte strings already support most of the same built-in operations as text strings.
# For example:
data = b'Hello world'
print(data[0:5])
# b'Hello'
print(data.startswith(b'Hello'))
# True
print(data.split())
# [b'Hello', b'world']
print(data.replace(b'Hello', b'Hello Cruel'))
# b'Hello Cruel world'

# Such operations also work with byte arrays. For example:
data = bytearray(b'Hello world')
print(data[0:5])
# bytearray(b'Hello')
print(data.startswith(b'Hello'))
# True
print(data.split())
# [bytearray(b'Hello'), bytearray(b'world')]
print(data.replace(b'Hello', b'Hello Cruel'))
# bytearray(b'Hello Cruel world')

# You can apply regular expression pattern matching to byte strings, but the patterns themselves need to
# be specified as bytes. For example:
data = b'FOO:BAR,SPAM'
import re
# print(re.split('[:,]', data))
# TypeError: cannot use a string pattern on a bytes-like object

print(re.split(b'[:,]', data))  # Notice: pattern as bytes
# [b'FOO', b'BAR', b'SPAM']

# Discussion
# For the most part, almost all of the operations available on text strings will work on byte strings.
# However, there are a few notable differences to be aware of.
# First, indexing of byte strings produces integers, not individual characters. For example:
a = 'Hello World'  # Text string
print(a[0])
# H
print(a[1])
# e

b = b'Hello World'  # Byte string
print(b[0])
# 72
print(b[1])
# 101

# This difference in semantic can affect programs that try to process byte-oriented data on a
# character-by-character basis.

# Second, byte strings don't provide a nice representation and don't print cleanly unless first
# decoded into a text string. For example:
s = b'Hello World'
print(s)
# b'Hello World'  # Observe b'...'
print(s.decode('ascii'))
# Hello World

# Similarly, there are no string formatting operations available to byte strings.
# print(b'{} {} {}'.format(b'ACME', 100, 490.1))
# AttributeError: 'bytes' object has no attribute 'format'

# If you want to do any kind of formatting applied to byte strings, it should be done using nomarl
# text strings and encoding. For example:
print('{:10s} {:10d} {:10.2f} ' . format('ACME', 100, 4901).encode('ascii'))
# b'ACME              100    4901.00 '

# Finally, you need to be aware that using a byte string can change the semantic of certain operations
# especially those related to the filesystem. For example, if you supply a filename encoded as bytes
# instead of a text string, it usually disables filename encoding/decoding. For example:
# Write a UTF-8 filename
with open('jalape\xf1o.txt', 'w') as f:
    f.write('spicy')

# Get a directory listing
import os
print(os.listdir('.'))
# 'jalapeño.txt'
print(os.listdir(b'.'))
# b'jalape\xc3\xb1o.txt'















