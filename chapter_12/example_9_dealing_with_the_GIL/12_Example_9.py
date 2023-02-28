"""
Dealing with the GIL(and how to stop worrying about it)
Problem
    You've heard the `Global Interpreter Lock(GIL)`, and are worried about that it might be
    affecting the performance of your multithread program.
Solution
    Parts of `C` implementation of the interpreter are not entirely thread-safe to a level of
    allowing concurrent execution.
    `GIL` only allows one Python thread execution at any given time.
    This lead to can't fully take advantage of multiple CPU cores.

    GIL仅仅影响CPU密集型任务，I/O密集型很少影响，I/O密集型任务就算建几千个线程也影响很小。

    1. Moving performance-critical code into C extension module, such as Numpy.
    2. Use PyPy, which features optimizations such as JIT compiler.

    *** Two strategies for working around the limitations of the GIL.
        1. use `multiprocessing` module to create a process pool and use it like coprocessor.
            the function `arguments` and return value must be compatible with `pickle`
            将CPU密集型任务放入ProcessPool运行，启动新的Python interpreter来工作，等待result返回时，将释放掉持有的GIL
        2. C extension programming. such as `ctypes` library
            C independent of Python, it releases the `GIL` when it's working.
Discussion
"""

__author__ = 'Frankie Fu'

import multiprocessing


# Example 1
# Perform a large calculation(CPU bound)
def some_work(args):
    ...
    # return result


# A thread that calls the above function
def some_thread():
    while True:
        ...
        # result = some_work(args)


# Use pool
pool = multiprocessing.Pool()


def some_thread_by_pool():
    while True:
        ...
        # pool.apply(some_work, (args,))
