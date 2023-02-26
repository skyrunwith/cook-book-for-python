"""
Performing simple Parallel Programming
Problem
    You have a program that performs a lot of CPU-intensive work, and you want it run faster
    by having it take advantage of multiple CPUS.
Solution
    `concurrent.futures` library `ProcessPoolExecutor`
Discussion
    Typical Usage of a `ProcessPoolExecutor`
        from concurrent import futures

        with futures.ProcessPoolExecutor as pool:
            do work in parallel using pool
"""

__author__ = 'Frankie Fu'
