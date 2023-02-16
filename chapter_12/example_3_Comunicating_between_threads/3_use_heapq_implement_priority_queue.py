import heapq
import threading


class PriorityQueue:
    def __init__(self):
        self._queue = []
        self._count = 0
        self._cv = threading.Condition()

    def put(self, priority, item):
        with self._cv:
            heapq.heappush(self._queue, (-priority, self._count, item))
            self._count += 1
            self._cv.notify()

    def get(self):
        with self._cv:
            if len(self._queue) == 0:
                self._cv.wait()
            return heapq.heappop(self._queue)[-1]


_sentinel = object()


def producer(n, out_q):
    while n > 0:
        out_q.put(-n, n)
        n -= 1


def consumer(in_q):
    while True:
        n = in_q.get()
        print(n)


q = PriorityQueue()
producer = threading.Thread(target=producer, args=(5, q))
consumer = threading.Thread(target=consumer, args=(q,))
producer.start()
consumer.start()
