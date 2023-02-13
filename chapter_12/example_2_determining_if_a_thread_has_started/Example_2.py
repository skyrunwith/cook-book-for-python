"""
Problem
    You've launched a thread, but want to know when it actually `starts running`.
Solution
    1. Use the `Event` object from the `threading` library.
        `Event` instances are similar to a `sticky` flag that allows threads to wait for something
        to happen(类似java的Object.wait, notify...).
        If event is unset, a thread will block on the event until the event get set.

        Object.wait() Object.notify()/Object.notifyAll().
        Or Condition.await() and Condition.signal()/Condition.signalAll() for Java 5+.
Discussion
    `Event` Object are best used for `one-time events`. It maybe leads to missed events, deadlock, or other problems.

    `Condition` object: If a thread is going to repeatedly signal an event over and over,
    `Condition` object probably better.

    Semaphores Object: If you are writing a program where you want to `wake up one waiting thread`. It' better to use
    a `Semaphores` or `Condition`.

    A more sane approach is to thread threads as communication tasks use `queues` or as actors.
"""

