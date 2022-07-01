#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""  """

__author__ = 'Frankie Fu'
# mypackage/A/spam.py
from . import grok
from .. B import bar
# import grok  # Error (not found)
from mypackage.A import grok  # OK

print(dir())
