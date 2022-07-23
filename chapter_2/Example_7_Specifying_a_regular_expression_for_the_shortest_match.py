#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Specifying a Regular Expression for the Shortest Match
Problem
    You're trying to match a text pattern using regular expressions, but it is identifying the longest
    possible matches of a pattern. Instead, you would like to change it to find the shortest possible match.
Solution
    add the "?" modifier after the "*" operator in the pattern, like this:
        r'\"(.*?)\"'
Discussion
    This recipe addresses one of the more common problems encountered when writing regular expressions involving
    the dot (.) character. In a pattern, the dot matches any character except a newline, However, if you bracket
    the dot with starting and ending text(such as a quote). matching will try to find the longest possible match
    to the pattern, This causes multiple occurrences of the starting or ending text to be skipped altogether and
    included in the results of the longer match. Adding the "?" right after operators such as "*" or "+" forces
    the matching algorithm to look for the shortest possible match instead.
"""

__author__ = 'Frankie Fu'
import re

# Solution
# This problem often arises in patterns that try to match text enclosed inside a pair of starting
# and end delimiters(eg. a quoted string). To illustrate, consider this example:
str_pat = re.compile(r'\"(.*)\"')
text1 = 'Computer says "no."'
print(str_pat.findall(text1))
# ['no.']
text2 = 'Computer says "no." Phone says "yes."'
print(str_pat.findall(text2))
# ['no." Phone says "yes.']

# In this example, the pattern r'\"(.*)\"' is attempting to match text enclosed inside quotes.
# However, the * operator in regular expression is greedy. so matching is based on finding the
# longest possible match. Thus in the second example involving text2, it incorrectly matches
# the two quoted strings.

# To fix this add the "?" modifier after the * operator in the pattern, like this:
str_pat = re.compile(r'\"(.*?)\"')
print(str_pat.findall(text2))
# ['no.', 'yes.']
# This makes the matching nongreedy, and produces the shortest match instead.




















