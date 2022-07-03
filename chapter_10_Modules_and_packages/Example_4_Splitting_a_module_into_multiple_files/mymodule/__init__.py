#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""  """

__author__ = 'Frankie Fu'


# version 1
# from .a import A
# from .b import B

# Lazy load version
def A():
    from .a import A
    return A()


def B():
    from .b import B
    return B()
