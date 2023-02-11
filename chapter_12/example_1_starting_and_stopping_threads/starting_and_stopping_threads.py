#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Problem
    You want to create and destroy threads for concurrent execution of code.
Solution
    threading library can be used to execute any Python callable in its own thread.
    create a Thread and supply the callable that you wish to execute as a target.
    Thread(target=, args=*, damon=), start(), is_alive(), join().
"""

__author__ = 'Frankie Fu'
import time


# Solution
# Code to execute in an independent thread
def countdown(n):
    while n > 0:
        print('T-minus', n)
        n -= 1
        time.sleep(5)


# Crete and launch a thread
from threading import Thread, current_thread

t = Thread(target=countdown, args=(10,))
# t.start()
# query thread instance to see if it's still running
if t.is_alive():
    print('Still Running')
else:
    print('Completed')

# waits for it to terminate
# t.join()

# 如果上一个thread没有join，那么两个线程会交替执行
# For long-running threads or background tasks that run forever
print('daemon')
# t = Thread(target=countdown(10, ), daemon=True)
# t.start()

