#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Normalizing Unicode Text to a Standard Representation
Problem
    You're working with Unicode strings, but need to make sure that all of the strings have the
    same underlying representation.
Solution

Discussion
"""

__author__ = 'Frankie Fu'

# Solution
# In Unicode, certain characters can be represented by more than one valid sequence of code points.
# To illustrate, consider the following example:
s1 = 'Spicy Jalape\u00f1o'
s2 = 'Spicy Jalapen\u0303o'
print(s1)
# Spicy Jalapeño
print(s2)
# Spicy Jalapeño

print(s1 == s2)
# False

print(len(s1))
# 14
print(len(s2))
# 15

# Here the text "Spicy Jalapeño" has been presented in two forms. The first uses the fully composed
# "ñ" character(U+00F1). The second uses the Latin letter "n" followed by a "~" combining character(U+0303)

# Having multiple representations is a problem for programs that compare strings. In order to fix this, you
# should first normalize the text into a standard representation using the unicodedata module:
import unicodedata

t1 = unicodedata.normalize('NFC', s1)
t2 = unicodedata.normalize('NFC', s2)
print(t1 == t2)
# True
print(ascii(t1))
# 'Spicy Jalape\xf1o'

t3 = unicodedata.normalize('NFD', s1)
t4 = unicodedata.normalize('NFD', s2)
print(t3 == t4)
# True
print(ascii(t3))
# 'Spicy Jalapen\u0303o'

# The first argument to "normalize()" specifies how you want the string normalized. "NFC" means that characters
# should be fully composed(i.e, use a single code point if possible). "NFD" means that characters should be fully
# decomposed with the use of combining characters.

# Python also supports the normalization forms "NFKC" and "NFKD", which add extra compatibility
# features for dealing with certain kinds of characters. For example:
s = '\ufb01'  # A single character
print(s)
# ﬁ

print(unicodedata.normalize('NFD', s))
# ﬁ

# Notice how the combined letters are broken apart here
print(unicodedata.normalize('NFKD', s))
# fi
print(unicodedata.normalize('NFKC', s))
# fi

# Discussion
# Normalization is an important part of any code that needs to ensure that it processes Unicode text in
# a sane and consistent way. This is especially true when processing strings received as part of user
# input where you have little control of the encoding.

# Normalization can also be an important part of sanitizing and filtering text. For example, suppose you
# want to remove all diacritical marks from some text(possibly for the purpose of searching or matching):
t1 = unicodedata.normalize('NFD', s1)
print(t1)
# Spicy Jalapeño
print(''.join(c for c in t1 if not unicodedata.combining(c)))
# Spicy Jalapeno

# This last examples shows another important aspect of the 'unicodedata' module--namely, utility functions
# for testing characters against charter classes. The 'combining()' function tests a character to see if it
# a combining character. There are other functions in the module for finding character categories, testing
# digits, and so forth.

# Unicode is obviously a large topic. For more detailed reference information about normalization,
# Visit Unicode's page on the subject.(http://www.unicode.org/faq/normalization.html). Ned Batchelder
# has also given an excellent presentation on Python Unicode handling issues at
# his website.(http://nedbatchelder.com/text/unipain.html)












