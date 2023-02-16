"""
Problem
    You have multiple threads in your program, and you want to communicate or exchange data between them.
Solutions
    Queue library: Perhaps the safest way to send data from one thread to another thread is to
    use `Queue` from the `Queue` library.
        Queue.get(), Queue.put

    How shutdown producer and consumer use queue.
        place a special sentinel to queue, consumer code use if condition check item is sentinel.
        Note, 需要考虑多个consumer的情况，所以消费了sentinel之后，还需要将sentinel放回队列，让consumer一个接一个的停止。

    虽然queue是最通用的线程通信方法，但你可以通过Condition来实现Locking和synchronization。
        For example, build thread-safe priority queue. Recipe 1.5()
        Use `heapq`, `Condition`

    queue.task_done(), queue.join(): 提供基本完成的特性。

    queue with event: producer会立刻知道consumer处理完成。

Discussion
    Queue doesn't make a copy of item. Thus, If you concerned about shared state, it may make sense to only pass
    `immutable data structure(e.g. integers, strings, or tuples)`, or to make deep copies of the queue items.
"""