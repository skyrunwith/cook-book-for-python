from threading import Event


def producer(n, out_q):
    while n > 0:
        e = Event()
        # Make an (data, event) pair and handle it to the consumer
        out_q.put((n, e))
        n -= 1
        # Wait for the consumer to process data
        e.wait()


def consumer(in_q):
    while True:
        (n, event) = in_q.get()
        # Indicate completion
        event.set()
