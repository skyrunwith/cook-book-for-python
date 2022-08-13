#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Packing and Unpacking Large Integers from Bytes
Problem
    You have a byte string and you need to unpack it into an integer value. Alternatively, you need to
    convert a large integer back into a byte string.
Solution
    int.from_bytes()
    int.to_bytes()
    int.big_length()
    struct module.
Discussion
"""

__author__ = 'Frankie Fu'

# Solution
# Suppose your program needs to work with a 16-element byte string that holds a 128-bit integer value.
# For example:
data = b'\x00\x124V\x00x\x90\xab\x00\xcd\xef\x01\x00#\x004'

# To interpret bytes as an integer, use 'int.from_bytes()', and specify the byte ordering like this:
print(len(data))
# 16
print(int.from_bytes(data, 'little'))
# 69120565665751139577663547927094891008
print(int.from_bytes(data, 'big'))
# 94522842520747284487117727783387188

# To convert a large integer value back into a byte string, use the 'int.to_bytes()' method, specifying
# the number of bytes and the byte order. For example:
x = 94522842520747284487117727783387188
print(x.to_bytes(16, 'big'))
# b'\x00\x124V\x00x\x90\xab\x00\xcd\xef\x01\x00#\x004'
print(x.to_bytes(16, 'little'))
# b'4\x00#\x00\x01\xef\xcd\x00\xab\x90x\x00V4\x12\x00'

# Discussion
# Converting large integer values to amd from byte strings is not a common operation.
# However, it sometimes arise in certain application domains, such as cryptography or
# networking. For instance, IPv6 network addresses are represented as 128-bit integers.
# If you are writing code that needs to pull such  values out of a data record, you might
# face this problem.

# As an alternative to this recipe, you might be inclined to unpack values using the 'struct' module,
# as described in Recipe 6.11. This works, but the siz of integers that can be unpacked with 'struct' is limited.
# Thus, you would need to unpack multiple values and combine them to create the final value. For example:
print(data)
# b'\x00\x124V\x00x\x90\xab\x00\xcd\xef\x01\x00#\x004'
import struct

hi, lo = struct.unpack('>QQ', data)
print(hi, lo)
# 5124093560524971 57965157801984052
print((hi << 64) + lo)
# 94522842520747284487117727783387188

# The specification of the byte order ('little or big') just indicates whether the bytes that make up
# the integer value are listed from the least to most significant or the other way around. This is
# easy to view using a carefully crafted hexadecimal value:
x = 0x1020304
print(x.to_bytes(4, 'big'))
# b'\x01\x02\x03\x04'
print(x.to_bytes(4, 'little'))
# b'\x04\x03\x02\x01'

# If you try to pack an integer into a byte string, but it won't fit, you'll get an error. You can use the
# 'int.git_length()' method to determine how many bits are required to store a value if needed:
x = 523 ** 23
print(x)
# 335381300113661875107536852714019056160355655333978849017944067
# print(x.to_bytes(16, 'little'))
# OverflowError: int too big to convert
print(x.bit_length())
# 208
nbytes, rem = divmod(x.bit_length(), 8)
if rem:
    nbytes += 1

print(x.to_bytes(nbytes, 'little'))
# b'\x03X\xf1\x82iT\x96\xac\xc7c\x16\xf3\xb9\xcf\x18\xee\xec\x91\xd1\x98\xa2\xc8\xd9R\xb5\xd0'

