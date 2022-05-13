#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Problem
    You want to iterate over a sequence, but would like to keep track of which element of the sequence
    is currently being processed.
Solution
    built-in enumerate()
    useful for tracking of line numbers in file.
Discussion
    enumerate more elegant.
    # keep your own counter variable
    lineno = 1
    for line in f:
        lineno +=1
    # enumerate()
    for lineno, line in enumerate(f):
        ...

    enumerate() return an successive tuples consisting of a counter and the value returned
    by calling next() on the sequence you've passed in.
"""

__author__ = 'Frankie Fu'

# Solution
from collections import defaultdict

my_list = ['a', 'b', 'c']
for idx, val in enumerate(my_list):
    print(idx, val)


# start the numbering at 1 instead of 0
for idx, val in enumerate(my_list, 1):
    print(idx, val)


# Case of tracking line numbers in files should you want to use a line number in an error message
def parse_data(filename):
    with open(filename, 'rt') as f:
        for lineno, line in enumerate(f, 1):
            fields = line.split()
            try:
                count = int(fields[1])
            except ValueError as e:
                print('Line {}: Parse error: {}'.format(lineno, e))


parse_data('data/enumerate_file.txt')


# enumerate() can be handy for keeping track of the offset into a list for occurrences of certain values.
# for example. map words in a file to the lines in which they occur.
word_summary = defaultdict(list)
with open('data/myfile.txt', 'r') as f:
    lines = f.readlines()

for idx, line in enumerate(lines):
    # Create a list of words in current line
    words = [w.strip().lower() for w in line.split()]
    for word in words:
        word_summary[word].append(idx)

print(word_summary)


data = [(1, 2), (3, 4), (5, 6), (7, 8)]

# Correct!
for n, (x, y) in enumerate(data):
    print(n, (x, y))
# Error
# for n, x, y in enumerate(data):
#     print(n, x, y)
