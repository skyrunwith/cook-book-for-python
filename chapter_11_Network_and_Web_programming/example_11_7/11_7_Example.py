"""
Communicating simply Between Interpreters
Problem
    You are running multiple instance of the Python interpreter, possibly on different machines,
    and you would like to exchange data between interpreters using messages.
Solution
    It is easy to communicate between interpreters if you use the `multiprocessing.connection` module.
    Here is a simple example of writing an echo server:
        11_7_1_echo_server.py

    Here is a simple example of a client connecting to the server and sending various messages.
        11_7_2_echo_client.py

    Unlike a low-level socket, messages are kept intact(each object sent using `send` is received
    in its entirety with `recv`). In addition, objects are serialized using `pickle`. So any object
    compatible with `pickle` can be sent or received over the connection.
Discussion
    There are many packages and libraries related to various forms of messages passing, sucha as
    `ZeroMQ`, `celery`, and so forth. As an alternative, you might also be inclined to implement
    a message layer on top of low-level sockets. However, sometimes you just want a simple solution.
    The `multiprocessing.connection` library is just that -- use a few simple primitives, you can
    easily connect interpreters together have them exchange messages.

    If you know that interpreters are going to be running on the same machine, you can use
    alternative forms of networking. such as UNix domain sockets and Windows named pipes.
    To create a connection using a Unix domain socket, simply change the address to a filename.
        s = Listener('/tmp/myconn', authkey=b'peekaboo')

    To create a connection using a Windows named pipes, use a filename:
        s = Listener(r'\\.\pipe\myconn', authkey=b'peekaboo')

    As a general rule, you would not be using `multiprocess` to implement `public-facing` services.
    The `authkey` parameter to `Client()` and `Listener()` is there to authenticate the end points
    of the connection. Connections with a bad key raise an exception. In addition, the module is
    probably best suited for long-running connections(not a large number of short connections).
    For example, two interpreters establish a connection and keep the connection active for
    the entire duration of a problem.

    Don't use `multiprocessing` if you need more low-level control over aspects of the connection.
    For example, you needed to support timeouts, nonblocking IO, or anything similar. you are probably
    better off using different library or implementing such features on top of socket instead.
"""

__author__ = 'Frankie Fu'
