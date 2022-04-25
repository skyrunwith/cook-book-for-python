#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Problem
    You have built a custom container object that internally holds a list, tuple, and some other iterable.
    You would like to iteration work with your new container.
Solution
    1. define __iter__ method that delegates iteration to the internally held container.
Discussion
    1. __iter__ return a special iterator object.
    2. __next__ carry out the actual iteration.
    3. iter(s) simple returns the underlying iterator by calling s.__iter__()
"""

__author__ = 'Frankie Fu'


class Node:
    def __init__(self, value):
        self._value = value
        self._children = []

    def __repr__(self):
        return f'Node({self._value})'

    def add_child(self, child):
        self._children.append(child)

    def __iter__(self):
        return iter(self._children) # iterable protocol forwards to the internally held _children attribute


if __name__ == '__main__':
    root = Node(0)
    node1 = Node(1)
    node2 = Node(2)
    root.add_child(node1)
    root.add_child(node2)
    for n in root:
        print(n)