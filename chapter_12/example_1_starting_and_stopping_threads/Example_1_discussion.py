#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Discussion
    Due to global interpreter lock(GIL). python only allows one thread to execute in interpreter at any given time.
    So python threads should generally not be used for computationally intensive tasks where you are trying to achieve
    parallelism on multiple CPUS.
    They are much better suited for I/O handling and concurrent execution in code that performs blocking operations
    (e.g, waiting for I/O, waiting for results from a database, ect.).

    inheritance from the Thread class.

    multiprocessing
"""

__author__ = 'Frankie Fu'

import time
from threading import Thread


class CountDownThread(Thread):
    def __init__(self, n):
        super().__init__()
        self.n = n

    def run(self):
        while self.n > 0:
            print('T-minus', self.n)
            self.n -= 1
            time.sleep(5)


# c = CountDownThread(5)
# c.start()


#
import multiprocessing
from chapter_12.example_1_starting_and_stopping_threads.terminate_threads import CountdownTask

# c = CountdownTask()
# p = multiprocessing.Process(target=c.run, args=(5,))
# p.start()