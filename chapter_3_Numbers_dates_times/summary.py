#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""  """

__author__ = 'Frankie Fu'
"""
1. round() function.
2. decimal module.
3. format() function.
4. Working with binary, octal, hexadecimal integers:
    bin(), oct(), hex(), format(number, ['b'|'o'|'x']?), int(str, base) 
5. Packing and unpacking large integers from bytes
    int.from_bytes()
    int.to_bytes()
    int.big_length()
    struct module.
6. Performing Complex-valued math:
    1. complex(real, imag) or 1+2j: 定义虚数
    2. numpy.array(): make arrays of complex values and perform operations.
    3. cmath.sqrt: could produces complex numbers.(python 标准计算是不会产生虚数的，所以要使用cmath库)
7. Working with infinity and NaNs
    1. use float(): float('inf'), float('-inf'), float('nan')
    2. math.isinf(), math.isnan()
    3. inf and 和正常数字计算，都会产生inf, inf/inf == 0.0
       nan 与任何数计算都为 nan
       inf + inf == nan
8. Calculating with fractions
    fraction module.
9. Calculating with large arrays.
    numpy module.
10. Performing matrix and linear algebra calculations
    np.matrix()
    m.T, m.I
    np.linalg
11. Picking thing at random
    random.choice(): pick a random item out of a sequence.
    random.sample(): To take a sampling of N items where selected items are removed from further consideration.
    random.shuffle(): If you simply want to shuffle items in a sequence in place.
    random.randint(): To produce random integers.
    random.random(): To produce uniform floating-point values in the range 0 to 1.
    random.getrandbits(): To get N random-bits expressed as an integer.
    random.seed(): alter the initial seed.
12. Converting days to seconds and other basic time conversions.
     datetime module:
        timedelta: days, seconds, total_seconds()
        datetime is aware of leap year.
    dateutil module.
13. Determining last friday's date
    custom get_previous_byday() function.
    dateuti.relativedelta.
14. Finding the date range for the current month
    datetime.timedelta()
    calendar.monthrange()
15. Converting strings into datetimes.
    datetime.strptime()
    datetime.strftime()
    faster solution:
        If you are parsing a lot of dates in your code and you know the precise format, you will probably
        format, you will probably get much 'better performance' by cooking up a custom solution instead.
"""