#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""  """

__author__ = 'Frankie Fu'

import pkgutil

print('__package__: ', __package__)
data = pkgutil.get_data(__package__, 'somedata.dat')
print(data)