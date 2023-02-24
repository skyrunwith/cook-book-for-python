"""
Locking with Deadlock avoidance
Problem
    Multiple threads acquire more than one lock at a time while avoiding deadlock.

    For instance, if a thread acquire the first lock, but then blocks try to acquire the second
    lock, that thread can block the process of other threads and make the program freeze.
Solution
    Use `context manager`
        Assign each lock a unique number, and to enforce an ordering rule
        that only allows multiple locks to be acquired in ascending order.

        Detect Deadlock.
Discussion
    If only one lock at a time, program will be deadlock free, However, if multiple locks
    at them same time, all bets(赌) are off.
"""

__author__ = 'Frankie Fu'

