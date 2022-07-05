#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""  """

__author__ = 'Frankie Fu'
# Same as 'from . import b'
import importlib

b = importlib.import_module('.b', __package__)
print(b)
