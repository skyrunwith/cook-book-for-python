#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
4. Iterators and Generators.
Iteration is one of Python's strongest features. At a high leve, you might simply view iteration as a way
to process items in a sequence. However, there is so much more that is possible, such as creating your own
iterator objects, applying useful iteration patterns in the 'itertools' module, making generator functions.
and so forth. This chapter aims to address common problems involving iteration.
"""

__author__ = 'Frankie Fu'
"""
4.1. Manually Consuming an Iterator
    next() function: run the iterator, process items in an iterable.
    StopIteration exception
    iter(s): get an iterator. same as by calling s.__iter__()
4.2 Delegating Iteration
    iterable protocol:
        __iter__(): delegates iteration to the internally held container, return iterator object.
            return a special iterator object that implements a __next__ method() to carry out
            the actual iteration
    iterator protocol:
        __iter__() method: Return the iterator object itself.
        __next__() method: iterator object's method, carry out the actual iteration.
4.3 Creating New Iteration Patterns with Generators
    yield: turns a function into a generator.
    generator function feature:
        yield statement.
        only run in response to 'next' operations carried out in iteration. 
        Once a generator function returns, iteration stops.
4.4 Implementing the Iterator Protocol 
    to building custom objects which support iteration.
    
    1.yield and yield from 
    2.iterator protocol: 
        __iter__(): return a special iterator object that implements a __next__() operation and use a 'StopIteration'
        exception to signal completion.
4.5 Iterating In Reverse
    reverse() function.
        only works if the object has a size that can be determined.
        or if the object implements a __reversed() special method.
    __reversed__() method.
4.6 Defining Generator Functions with Extra State
    If you want a generator to expose extra state to the user, don't forget that you can easily implement it as
    a class, putting the 'generator function' code in the __iter__() method.
    
    1. use yield statement in __iter__() method. 
4.7 Taking a Slice of an Iterator.
    To Take a slice of data produced by an iterator, but the normal slicing operator doesn't work.
    
    itertools.islice(): 
        1.consuming and discarding all of the items up to the starting slice index. Further items are
          then produced by the islice object until the ending index has been reached.
        2.islice() will consume data on the supplied iterator, iterator can't be rewound.
4.8 Skipping the First Part of an Iterable.
    To iterate over items in an iterable, but the first few items aren't of interest and 
    you just want to discard them.
    
    1.itertools.dropwhile(f):
        The returned iterator discards the 'first items' in the sequence as long as the supplied function returns True.
        Afterwards, the entirety of the sequence is produced.
    2.itertools.islice(): 
        skip exact number of items you want to skip.
    3.filtering: 
        discard all items if condition is True.
4.9 Iterating Over All Possible Combinations(组合) or Permutations(排列)
    1.itertools.permutations():
        takes a collection of items and produces a sequence of tuples that rearranges all of the items into
        all possible permutations.
    2.itertools.combinations():
        produce a sequence of combinations of items taken from the input.
    3.itertools.combinations_with_replacements():
        allow the same item to be chosen more than once.
4.10 Iterating Over the Index-Value Pairs of a Sequence.
    enumerate(): 
        keep track of which element of the sequence is currently being processed.
4.11 Iterating Over Multiple Sequences Simultaneously
    zip():
        iterate over more than one sequence simultaneously.
        create an iterator as a result.
    zip_longest()
    dict(zip())
    list(zip())
"""
