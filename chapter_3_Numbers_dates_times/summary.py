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
"""