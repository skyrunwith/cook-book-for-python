#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Formatting Numbers for Output
Problem
    You need to format a number for output, controlling the number of digits, alignment, inclusion of a thousands
    separator, and other details.
Solution
    Use built-in format() function.
        general form: '[<>^]'?width[,]?(.digits)?'
Discussion
    format works for both floating-point numbers and Decimal numbers.
"""

__author__ = 'Frankie Fu'

# To format a single number for output, use the built-in 'format()' function. For example:
x = 1234.56789

# Two decimal places of accuracy
print(format(x, '0.2f'))
# 1234.57
# Right justified in 10 chars, one-digit accuracy
print(format(x, '>10.1f'))
# '    1234.6'
# Left justified
print(format(x, '<10.1f'))
# '1234.6    '
# Centered
print(format(x, '^10.1f'))
# '  1234.6  '
# Inclusion of thousands of separator
print(format(x, ','))
# 1,234.56789
print(format(x, '0.1f'))
# 1234.6

# The general form of the width and precision in both cases is '[<>^]'?width[,]?(.digits)?' where width and digits
# are integer and ? signifies optional parts. The same format codes are also used in the . format() method of strings.
# For example:
print('The values is {:0.2f}'.format(x))
# The values is 1234.57

# Discussion
# Formatting numbers for output is usually straightforward. The technique shown works for both floating-point numbers
# and Decimal numbers in the 'decimal' module.

# When the number of digits is restricted, values are rounded away according to the same rules of the 'round()'
# function. For example:
print(x)
# 1234.56789
print(format(x, '0.1f'))
# 1234.6
print(format(-x, '0.1f'))
# -1234.6

# Formatting of values with a thousands separator is not locale aware. If you need to take into account, you might
# investigate functions in the 'locale' module. You can also swap separator characters using the translate() method
# of string. For example:
swap_separators = {ord('.'): ',', ord(','): "."}
print(format(x, ',').translate(swap_separators))
# 1.234,567891.234,56789

# In a lot of Python code, numbers are formatted using the % operator. For example:
print('%0.2f' % x)
# 1234.57
print('%10.1f' % x)
# '    1234.6'
print('%-10.1f' % x)
# '1234.6    '

# This formatting is still acceptable, but less powerful than the more modern 'format()' method. For example,
# some features(e.g, adding thousands separators) aren't supported when using the % operator to format operator.
