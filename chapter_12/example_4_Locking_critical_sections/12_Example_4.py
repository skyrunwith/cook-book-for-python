""" 
Problem
    Your program uses threads, and you want to lock critical sections of code to avoid `race condition`
Solution
    Use `Lock` object, to make mutable object safe to use by multiple threads.
        A `Lock` guarantees `mutual exclusion` when used the `with` statement.
Discussion
    To avoid `deadlock`, each thread is only allowed to acquire one lock at a time. It this is not possible, Recipe 12.5
    introduce more advanced deadlock avoidance.

    Synchronization primitives: such as `RLock` and `Semaphore`.

    Class level `Lock`: Class variant.

    `Semaphore`

    If you are interested in the underlying theory and implementation of `synchronization primitives`, consult almost
    any textbook on operating systems.
"""


__author__ = 'Frankie Fu'