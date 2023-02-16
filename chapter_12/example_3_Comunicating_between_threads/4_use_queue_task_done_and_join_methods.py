import threading
from queue import Queue


def producer(n, out_q):
    while n > 0:
        out_q.put(n)
        n -= 1


def consumer(in_q):
    while True:
        n = in_q.get()
        print(n)
        in_q.task_done()


q = Queue()
p = threading.Thread(target=producer, args=(5, q))
c = threading.Thread(target=consumer, args=(q,))
p.start()
c.start()
q.join()
