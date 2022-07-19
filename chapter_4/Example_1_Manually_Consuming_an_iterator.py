#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Problem
    if you can't and don't want use a for loop, you need to process items in an iterable.
Solution
    1. use next function(), catch StopIteration and exception
    2. return a terminating value
    3. precise control over underlying iteration
"""

__author__ = 'Frankie Fu'


def use_iterable():
    print('### use_iterable')
    """
    use next function(), catch StopIteration and exception
    """
    with open("data/passwd.txt", 'r') as f:
        try:
            while True:
                line = next(f)
                print(line, end='')
        except StopIteration:
            pass


use_iterable()


def iterable_return_terminating_value():
    """
    return a terminating value
    :return:
    """
    print("### iterable_return_terminating_value")
    with open('data/passwd.txt') as f:
        while True:
            line = next(f, None)
            if line is None:
                break
            print(line, end='')


iterable_return_terminating_value()


def precise_control_underlying_iteration():
    print("### precise control over underlying iteration")
    items = [1, 2, 3]
    # Get the iterator
    it = iter(items)  # invoke items.__iter__()
    # Run the iterator
    print(next(it))  # Invoke it.__next__()
    print(next(it))
    print(next(it))
    print(next(it))  # Raise StopIteration


precise_control_underlying_iteration()