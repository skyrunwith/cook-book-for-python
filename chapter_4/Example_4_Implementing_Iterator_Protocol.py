#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Problem
    You are building custom objects on which you would like to support iteration.
    but would like an easy way to implement the iterator protocol.
Solution
    1. the easiest way to implement iteration on an object is to use a generator function.
Discussion
    1. Python's iterator protocol requires __iter__() to return a special iterator object that implements
        a __next__() operation and uses a StopIteration exception to signal completion.
"""

__author__ = 'Frankie Fu'


# Implements an iterator that traverses nodes in a depth-first pattern.
class Node:
    def __init__(self, value):
        self._value = value
        self._children = []

    def __repr__(self):
        return f'Node({self._value})'

    def add_child(self, node):
        self._children.append(node)

    def __iter__(self):
        return iter(self._children)

    def deep_first(self):
        """ yield, yield from """
        yield self
        for c in self:
            yield from c.deep_first()


if __name__ == '__main__':
    root = Node(0)
    child1 = Node(1)
    child2 = Node(2)
    root.add_child(child1)
    root.add_child(child2)
    child1.add_child(Node(3))
    child1.add_child(Node(4))
    child2.add_child(Node(5))
    for node in root.deep_first():
        print(node)
