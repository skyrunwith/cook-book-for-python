""" 
Concurrency

Python has long supported different approaches to concurrent programming, including
programming with `threads`, launching `subprocesses`, and various tricks involving `generator functions`.
In this chapter, recipes related to various aspects of concurrent programming are presented, including
common thread programming techniques and approaches for parallel processing.

As experienced programmers know, concurrent programming is fraught with potential peril. Thus, a major focus
of this chapter is on recipes that tend to lead to more reliable and debuggable code.
"""

__author__ = 'Frankie Fu'
"""
12.1 Starting and Stopping Threads
    `threading` library: Create a `Thread` instance and supply the callable function.
        Thread(target=, args=*, damon=), start(), is_alive(), join().
    Need to build features by self.
        terminate a thread, 
        signal a thread, 
        adjust it's scheduling, 
        perform any other high-level operations.
    GIL(Global interpreter lock): Python threads are restricted to an execution model that only allows one thread 
    to execute in the interpreter at any given time.
        Python threads 不适合并发执行CPU密集型任务，Python threads 更适合处理I/O和其他处理并发执行的Blocking Operations
        (e.g., waiting for I/O, waiting for results from a database, etc.)
    Inherit from `Thread` class:
        缺点：只能在`threads`的上下文中使用，不能移植到`multiprocess`中.
12.2 Determining if a thread has started.
    Event Object: used for `ont-time` events
        Event.set(), Event.wait(), Event.clear(), Event.is_set()
    Condition Object: used for repeatedly on an event over and over
        Condition.acquire(), .release(), .wait(), .wait_for(), .notify(), .notify_all(), 
    Semaphore Object: used for wake up one waiting thread.
        Semaphore.acquire(), Semaphore.release().
12.3 Communicating_between_threads.
    Use `queue.get()`, `queue.put()`
    Use a _sentinel object to shutdown `queue` consumer.
    Use `heapq` with `Condition` to implement Priority Queue
    Use `queue.task_done()`, `queue.join()` implement basic completion feature.
    Use `queue` with `Event` to implement consumer to notify producer.
    Queue with immutable data structures, `deepcopy item`
    Queue block and timeout.
"""
