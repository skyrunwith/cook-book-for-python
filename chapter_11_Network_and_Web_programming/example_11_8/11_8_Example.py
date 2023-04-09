"""
Implementing Remote Procedure Calls
Problem
    You want to implement simple Remote Procedure Calls(RPC) on top of a message passing layer,
    such as sockets, multiprocessing connections, ZeroMQ.
Solution
    RPC is easy to implement by encoding `function request, arguments, and returned values` using pickle,
    and passing the pickled byte strings between interpreters. Here is an example of a simple RPC handler
    that could be incorporated into a server.
    11_8_1_rpcserver.py

    To use this handler, you need to add it into a message server. There are many possible choices, but
    the `Multiprocessing` library provides a simple option. Here is an example `RPC` server.
    11_8_1_rpcserver.py

    To access the server, you need to create a corresponding Proxy class that forwards requests. For example
    11_8_2_client.py

    To use the proxy, you wrap it around the connection to the server. For example:
    11_8_2_client.py

    It should be noted that many message passing layer(Such as multiprocessing) already serialized data
    using pickle. It this is the case, the pickle.dumps() and pickle.loads() calls can be eliminated.
Discussion
    The general idea of `RPCHandler` and `RPCProxy` is relatively simple. If a client wants to call
    a remote function such as `foo(1, 2, z=3)`, the proxy class create a tuple ('foo', (1, 2), {'z': 3})
    that contains the function name and arguments. This tuple is pickled and sent over the connection.
    This is performed in the `do_rpc` closure that returned by `__getattr__` method of RPCProxy.
    The server received and unpickled the message, and look up the function name to see if it's registered,
    and execute it with the arguments. The result(or Exception) is then pickled and sent back.

    As shown, the process relies on `multiprocessing` for communication. However, this could be made to work
    with just about any other messaging system. For example, if you want to implement it over ZeroMQ, just
    replace the connection objects with an ZeroMQ sockets object.

    Given the reliance on `pickle`, security is a major concern(because a clever hacker can create messages
    that makes arbitrary function execute during unpickling). In particular, you should not allow RPC
    from untrusted and unauthenticated clients. In particular, you definitely don't want to allow RPC
    access from just any machine on the Internet--This should really only be internally, behind a firewall,
    and not exposed to the rest of the world.

    As an alternative to `pickle`, you might consider the use of JSON, XML, or other data encoding for serialization.
    For example, this recipe is fairly easy to adapt to JSON encoding if you simply replace
    `json.dumps` with `pickle.dumps` and `json.loads` with `pickle.loads`.

    One complicated factor in implementing RPC is how to handle exceptions. At the very least, the server
    should not crash if an Exception raised by a method. The means by which the exception gets reported back
    to the client requires study. If you're using pickle, the exception instance can be often serialized
    and reraised in the client. If you're using some other protocol, you might have think of an alternative
    approach. At the very least, you probably want to return the exception string in the response. This is
    the approach taken in JSON example.

    For another example of an RPC implementation, it can be useful to look the implementation of
    the `SimpleXMLRPCServer` and the `ServerProxy` classes used in XML-RPC. as described in Recipe 11.6.
"""

__author__ = 'Frankie Fu'
