#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Solution
    terminate threads by yourself.
"""

__author__ = 'Frankie Fu'

import time
from threading import current_thread, Thread


# terminate threads, must be programmed to poll for exit at selected points.
class CountdownTask:
    def __init__(self):
        self._running = True

    def terminate(self):
        self._running = False

    def run(self, n):
        while self._running and n > 0:
            print(f'{current_thread().ident} T-minus', n)
            n -= 1
            time.sleep(5)


if __name__ == "__main__":
    c = CountdownTask()
    t3 = Thread(target=c.run, args=(10,))
    t3.start()
    time.sleep(10)
    c.terminate()  # Signal termination
    t3.join()  # Wait for actual termination (if needed)
