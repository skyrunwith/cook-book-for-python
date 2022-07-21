#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Matching Strings Using Shell Wildcard Patterns
Problem
    You want to match text using the same wildcard patterns as are commonly used when
    working in Unix shells(e.g., *.py, Dat[0-9]*.csv, etc.)
Solution
    "fnmatch" module provides two functions-- "fnmatch()" and "fnmatchcase()"--that can be used to perform
    such matching.
Discussion
    This matching performed by fnmatch sits somewhere between the functionality of simple string methods and
    the full power of regular expressions.
    If you're just to trying to provide a simple mechanism for allowing wildcards in data processing operations,
    it's often reasonable solution.
    If you're actually trying to write code that matches filenames, use the "glob" module instead. See Recipe 5.13.
"""

__author__ = 'Frankie Fu'

# Solution
from fnmatch import fnmatch, fnmatchcase

print(fnmatch("foo.txt", "*.txt"))

print(fnmatch("foo.txt", "?oo.txt"))

names = ['Data1.csv', 'Data2.csv', 'config.ini', 'foo.py']
print([name for name in names if fnmatch(name, 'Dat*.csv')])


# Normally, fnmatch() matches patterns using the same case-sensitivity rules as the system'
# underlying filesystem(which varies based on operating system). For example:
# On OS X (MAC)
print(fnmatch('foo.txt', '*.TXT'))
# False
print(fnmatch('foo.txt', '*.TXT'))
# True

# If this distinction matters, use "fnmatchcase()" instead. It matches exactly based on the lower- and uppercase
# conventions that you supply.
print(fnmatchcase('foo.txt', '*.TXT'))
# False

# An often overlooked feature of these functions is their potential use with data processing of
# nonfilename strings. For example, suppose you have a list of street addresses like this:
addresses = [
 '5412 N CLARK ST',
 '1060 W ADDISON ST',
 '1039 W GRANVILLE AVE',
 '2122 N CLARK ST',
 '4802 N BROADWAY']
# You could write list comprehension like this:
from fnmatch import fnmatchcase

print([addr for addr in addresses if fnmatchcase(addr, '* ST')])

print([addr for addr in addresses if fnmatchcase(addr, '54[0-9][0-9] *CLARK*')])

# Discussion
# This matching performed by fnmatch sits somewhere between the functionality of simple string methods
# and the full power of regular expressions. If you're just trying to provide a simple mechanism for
# allowing wildcards in data processing operations, it's often a reasonable solution.

# If you're actually trying to write code that matches filenames, use the glob module instead. See Recipe 5.13.








