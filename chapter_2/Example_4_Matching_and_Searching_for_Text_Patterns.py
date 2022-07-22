#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Matching and Searching for Text Patterns
Problem
    You want to match or search text for a specific pattern.
Solution
    If the text you're trying to match is a simple literal. you can often just use the basic string
    methods, such as "str.find(), str.endswith(), str.startswith(), or similar.

    For more complicated matching, use regular expressions and the 're module'.
        re.match(pattern, string)
        re.compile(pattern)
            match(string)
            findall(string)
            finditer(string) : If you want to matches iteratively.
    capture groups by enclosing parts of the pattern in parentheses.
Discussion
    re.compile()
        match(), findall(), finditer()
    re.match()
    re.findall()

    The module-level functions keep a  cache of recently compiled patterns. it skip the compilation step.
        module-level functions in the "re module" instead. such as re.findall().
"""

__author__ = 'Frankie Fu'

# Solution
text = 'yeah, but no, but yeah, but no, but yeah'

# Exact match
print(text == 'yeah')
# False

# Match at start or end
print(text.startswith('yeah'))
# True
print(text.endswith('no'))
# False
# Search for the location of the first occurrence
print(text.find('no'))
# 10

# For more complicated matching, use regular expressions and "re module". To illustrate the basic mechanics of
# using regular expressions, suppose you want to match dates specified as digits, such as '11/27/2012'.
# Here is a sample of how you would do it:
text1 = '11/27/202'
text2 = 'Nov 27, 2012'

import re

# Simple matching: \d+ mends match one or more digits
if re.match(r'\d+/\d+/\d+', text1):
    print('yes')
else:
    print('no')
# yes

if re.match(r'\d+/\d+/\d+', text2):
    print('yes')
else:
    print('no')
# no

# If you're going to perform a lot of matches using the same pattern, it usually pays to precompile the regular
# expression pattern into a pattern object first. For example:
datepat = re.compile(r'\d+/\d+/\d+')
if datepat.match(text1):
    print('yes')
else:
    print('no')
# yes
if datepat.match(text2):
    print('yes')
else:
    print('no')
# no

# "match()" always tries to find the match at the start of a string. If you want to search text for all occurrences
# of a pattern, use the "findall()" method instead. For example:
text = 'Today is 11/27/2012, PyCon starts 3/13/2013.'
print(datepat.findall(text))
# ['11/27/2012', '3/13/2013']

# When defining regular expressions, it is common to introduce capture groups by enclosing parts of
# the pattern in parentheses. For example:
datepat = re.compile(r'(\d+)/(\d+)/(\d+)')
# Capture groups often simplify subsequent processing of the matched text because the contents of
# each group can be extracted individually. For example:
m = datepat.match('11/27/2012')
print(m)
# <re.Match object; span=(0, 10), match='11/27/2012'>

# Extract the contents of each group
print(m.group(0))
# 11/27/2012
print(m.group(1))
# 11
print(m.group(2))
# 27
print(m.group(3))
# 2012
print(m.groups())
# ('11', '27', '2012')
month, day, year = m.groups()

# Find all matches (notice splitting into tuples)
print(text)
# Today is 11/27/2012, PyCon starts 3/13/2013.
print(datepat.findall(text))
for month, day, year in datepat.findall(text):
    print(f'{year}-{month}-{day}')
# 2012-11-27
# 2013-3-13

# The findall method searches the text and finds all matches, returning them as a list.
# If you want to find matches iteratively, use the finditer() method instead. For example:
for m in datepat.finditer(text):
    print(m.groups())
# ('11', '27', '2012')
# ('3', '13', '2013')

# Discussion
# A basic tutorial on the theory of regular expressions is beyond the scope of this bok.
# However, this recipe illustrates the absolute basics of using the 're module' match and search for text.
# The essential functionality is first compiling a pattern using 're.compile()' and then using methods such
# as "match(), findall(), or finditer().

# When specifying patterns, it is relatively common to use raw strings such as r'(\d+)/(\d+)/(\d+)'.
# Such strings leave the backslash character uninterpreted, which can be useful in the context of
# regular expressions. Otherwise, you need to use double backslashes such as '(\\d+)/(\\d+)/(\\d+)'

# Be aware that the "match()" method only checks the beginning of a string. It's possible
# that it will match things you aren't expecting. For example:
m = datepat.match('11/27/2012abcdef')
print(m)
# <re.Match object; span=(0, 10), match='11/27/2012'>
print(m.group())
# 11/27/2012

# If you want to exact match, make sure the pattern includes the end-marker($), as in  the following:
datepat = re.compile(r'(\d+)/(\d+)/(\d+)$')
print(datepat.match('11/27/2012abcdef'))
# None
print(datepat.match('11/12/2012'))
# <re.Match object; span=(0, 10), match='11/12/2012'>

# Be aware, though, that if you're going to perform a lot of matching or searching, it usually pays to
# compile the pattern first and use it over and over again. The module-level functions keep a cache of
# recently compiled patterns, so there isn't a huge performance hit, but you'll
# save a few lookups and extra processing by using your own compiled pattern.


































