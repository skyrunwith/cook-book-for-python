#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Working with Binary, Octal, and Hexadecimal Integers
Problem
    You need to convert or output integers represented by binary, octal, or hexadecimal digits.
Solution
    To convert an integer into a binary, octal, or hexadecimal text string, use the bin(), oct(), or hex() functions.
Discussion
"""

__author__ = 'Frankie Fu'

# Solution
x = 1234
print(bin(x))
# 0b10011010010
print(oct(x))
# 0o2322
print(hex(x))
# 0x4d2

# Alternatively, you can use the 'format()' function if you don't want the '0b, 0o, or 0x' prefixes to appear.
# For example:
print(format(x, 'b'))
# 10011010010
print(format(x, 'o'))
# 2322
print(format(x, 'x'))
# 4d2

# Integers are signed, so if you are working with negative numbers, the output will also include a sign.
# For example:
x = -1234
print(format(x, 'b'))
# -10011010010
print(format(x, 'x'))
# -4d2

# If you need to produce an unsigned value instead, you'll need to add in the maximum value to set the bit length.
# For example, to show a 32-bit value, use the following:
x = -1234
print(format(2**32 + x, 'b'))
# 11111111111111111111101100101110
print(len('11111111111111111111101100101110'))  # 32

print(format(2**32 + x, 'x'))
# 'fffffb2e'

# To convert integer strings in different bases, simply use the 'int()' function with an appropriate base.
# For example:
print(int('4d2', 16))
# 1234
print(int('10011010010', 2))
# 1234

# Discussion
# For the most part, working with binary, octal, and hexadecimal integers is straightforward. Just remember that these
# conversions only pertain to the conversion of integers to and from a textual representation. Under the covers,
# there's just one integer type.

# Finally, there is one caution for programmers who use octal. The Python syntax for specifying octal values is
# slightly different than many other languages. For example, if you try something like this, you'll get a syntax error:
import os
print(os.chmod('script.py', 0o755))



