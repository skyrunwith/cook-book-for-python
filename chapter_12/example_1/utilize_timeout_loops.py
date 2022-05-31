#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Solution
    Polling for thread termination can be tricky to coordinate if threads perform blocking operations such as I/O.
"""

__author__ = 'Frankie Fu'


class IOTask:
    def __init__(self):
        self._running = True

    def terminate(self):
        pass

    def run(self, sock):
        # sock is a socket:
        sock.settimeout(5)  # Set timeout period
        while self._running:
            # Perform a blocking I/O operation w/ timeout
            try:
                data = sock.recv(8192)
                break
            except sock.settimeout:
                continue
            # Continued processing
        # Terminated
        return
