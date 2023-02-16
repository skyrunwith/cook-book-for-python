import threading
import queue

"""
A subtle feature of this example is that the consumer, upon receiving the sentinel special value,
Immediately places it onto the queue. This propagates the sentinel to other consumers that might be 
listening on the same queue -- thus shutting them all down one after the other. 
"""


# Object that signals shutdown
_sentinel = object()


def producer(n, out_q: queue):
    while n > 0:
        out_q.put(n)
        print('Put', n)
        n = n - 1
    # put the sentinel on the queue to indicate completion
    out_q.put(_sentinel)


def consumer(in_q: queue):
    while True:
        n = in_q.get()
        # check for termination
        if n is _sentinel:
            in_q.put(_sentinel)
            break
        print('Get', n)


# Create the shared queue and launch both threads.
q = queue.Queue()
a = threading.Thread(target=producer, args=(5, q))
b = threading.Thread(target=consumer, args=(q,))
a.start()
b.start()
