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
12.4 Locking critical sections.
    Use Lock: function or methods or class level lock.
    RLock and Semaphore.
12.5 Locking with deadlock avoidance
    If need to ues more locks at a time, Use contextmanager implement ascending locks.
12.6 Storing Thead-Specific state
    threading.local()
12.7 Create a thread pool:
    concurrent.futures library's ThreadExecutorPool
    pool.submit().result()
    threading.stack_size: limit virtual memory size.
12.8 Performing simple parallel programming
    Cpu-intensive tasks.
    `ProcessPoolExecutor`
12.9 Dealing with the GIL(How to stop worrying about it)
     GIL仅仅影响CPU密集型任务，I/O密集型很少影响，I/O密集型任务就算建几千个线程也影响很小。
     Two strategies for working around the limitations of the GIL.
     1. use `multiprocessing` module to create a process pool and use it like coprocessor.
     2. C extension programming. such as `ctypes` library
12.10 Defining an actor task
    You'd like to define tasks with behavior similar to "actors" in the so-called "actor model".
    The "Actor model" is one of the oldest and most simple approaches to concurrency and distributed computing.
    "A Thread and A Queue" and a `send` method.s
    
12.11 Implementing Publish/Subscribe Message
    A separate `exchange` or `gateway` object that acts as an intermediary for all messages.
    A message send to `the exchange` and it delivers to one or more attached tasks.
    
    一般线程通信是用queue，但是pub/sub也有很多优点：
    First, Only worry about connecting them to a known `exchange`, decouple variety tasks, sucha as `logging` lib.
    Second, `Broadcast message` to multiple subscribers opens up new communication pattern.
    Next, it works with a variety of `task-like` object
    Next, use context-management protocol.
    Finally, there are numerous possible extensions to exchange idea.(Distributed computing system, routing
    message to task on different machine.)
"""
