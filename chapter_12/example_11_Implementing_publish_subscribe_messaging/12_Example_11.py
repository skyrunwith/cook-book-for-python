"""
Implementing publish/subscribe message
Problem
    You have program based on communicating threads and want them to implement publish/subscribe messaging.
Solution
    A separate `exchange` or `gateway` object that acts as an intermediary for all messages.
    A message send to `the exchange` and it delivers to one or more attached tasks.
Discussion
    The concepts of tasks or threads send messages to one another(often via queues) is easy
    to implement and quite popular. However, the benefits of using publish/subscribe(pub/sub) model
    instead are often overlooked.
        First. Simplify much of plumbing involved in setting up communicating threads. Instead of trying to
        wire threads together across (multiple program modules), you only worry about connecting them to
        a known `exchange`. It is similar `logging` library. It can make it easier to
        `decouple various tasks in the program`.

        Second. `Broadcast messages` to multiple subscribers opens up new communication patterns.
        For example, you could implement system with `redundant tasks, broadcasting, or fan-out`.
        You could also attach themselves to the exchange as an ordinary subscribers.

        Last but not least, it works with a variety of `task-like` object.(the receivers of message cloud be actors,
        coroutines, network connections, or anything that implements `send()` method)

        Use context-management protocol.(Because it is quite easy to forget the final `detach()` step).

        Finally, there are numerous possible extension to the exchange ideas.
"""

__author__ = 'Frankie Fu'