import threading
import queue


def producer(n, out_q: queue):
    while True:
        out_q.put(n)
        print('Put', n)
        break


def consumer(in_q: queue):
    while True:
        n = in_q.get()
        print('Get', n)
        break


# Create the shared queue and launch both threads.
q = queue.Queue()
a = threading.Thread(target=producer, args=(5, q))
b = threading.Thread(target=consumer, args=(q,))
a.start()
b.start()
