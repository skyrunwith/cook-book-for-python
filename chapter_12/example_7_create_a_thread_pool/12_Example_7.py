"""
Create a Thread Pool
Problem
    You want to create a pool of worker threads for serving clients or performing other
    kinds of work.
Solution
    `concurrent.futures` library `ThreadPoolExecutor` class.
    `ThreadPoolExecutor.submit()`
    'pool.submit().result()': one advantage of `ThreadPoolExecutor` over manually implementation pool.
Discussion
    创建大的线程池的一个可能需要关注的问题是内存的使用。 例如，如果你在OS X系统上面创建2000个线程，
    系统显示Python进程使用了超过9GB的虚拟内存。 不过，这个计算通常是有误差的。当创建一个线程时，
    操作系统会预留一个虚拟内存区域来 放置线程的执行栈（通常是8MB大小）。但是这个内存只有一小片段被实际映射到真实内存中。
    因此，Python进程使用到的真实内存其实很小 （比如，对于2000个线程来讲，只使用到了70MB的真实内存，而不是9GB）。
    如果你担心虚拟内存大小，可以使用 threading.stack_size() 函数来降低它。例如：
    threading.stack_size(65536)

"""