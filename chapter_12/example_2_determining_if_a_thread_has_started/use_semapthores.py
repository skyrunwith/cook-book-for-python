import threading
from threading import Semaphore


def workers(n, sema: Semaphore):
    # Wait to be signaled
    sema.acquire()
    # Do some work
    print('Worker', n)


#
sema = threading.Semaphore(0)

nworkers = 3

for n in range(nworkers):
    t = threading.Thread(target=workers, args=(n, sema,))
    t.start()
print('Release')
sema.release()
print('Release 2')
sema.release(2)




