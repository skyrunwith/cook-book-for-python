#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""" 
Problem
    You have a sequence of items, and you'd like to determine the most frequently occurring items in the sequence.
Solution
    collection.Counter():
        It even come with a handy "most_common()" method that will give you the answer.
        update method()
    mathematical operations.
        combine:
            words + morewords
        subtract:
            words - morewords
Discussion
    Counter objects are a tremendously useful tool for almost any kind of problem where you need to
    tabulate and count data. You should prefer this over manually written solutions involving dictionaries.
"""

__author__ = 'Frankie Fu'

# Let's say you have a list of words and you want to find out which words occur most often.
words = [
    'look', 'into', 'my', 'eyes', 'look', 'into', 'my', 'eyes',
    'the', 'eyes', 'the', 'eyes', 'the', 'eyes', 'not', 'around', 'the',
    'eyes', "don't", 'look', 'around', 'the', 'eyes', 'look', 'into',
    'my', 'eyes', "you're", 'under'
]

from collections import Counter

word_counts = Counter(words)
top_three = word_counts.most_common(3)
print(top_three)

# Discussion
# As input, Counter objects can be fed any sequence of hashable input items. Under the covers, a Counter is a
# dictionary that maps the items to the number of occurrences.
print(word_counts['not'])
print(word_counts['eyes'])

# If you want to increment the count manually, simple use dddtion.
morewords = ['why', 'are', 'you', 'not', 'looking', 'in', 'my', 'eyes']
for word in morewords:
    word_counts[word] += 1

print(word_counts['eyes'])

# Or, alternatively, you could use the update() method:
word_counts.update(morewords)
print(word_counts['eyes'])

# A little-known feature of Counter instance is that they can be easily combined using various mathematical operations.
a = Counter(words)
b = Counter(morewords)
print(a)

print(b)

# Combine counts
print(a + b)

# Subtract count
print(a - b)