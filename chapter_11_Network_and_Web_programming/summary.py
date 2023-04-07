""" 
Network and web programming

This chapter is about various topic related to using Python in networked and distributed applications.
Topics are split between using Python as client to access existing servers, and using Python to implement
networked services as a server. Common techniques for writing code involving cooperating and communicating
with interpreters are also given.
"""

__author__ = 'Frankie Fu'
"""
11.1 Interacting with HTTP Services as a client
    You need to access various services as a client.
    
    How to use `urllib` to access existing services.
    How to use `requests library` access existing services.
    All of this is much easier in `requests`(e.g., cookies, authentication, header, encoding, ect.)
        resp.text(the Unicode decoded text from a request)
        reps.content(the raw binary response content)
        reps.json(the response content interpreted as JSON)  
        
11.2. Creating TCP Server (A reliable connection)
    You want to implement server that communicates with clients using TCP internet protocol.
    
    `socketserver` lib :
        a handler method class:
            BaseRequestHandler, StreamRequestHandler.
        server:
            TCPServer, ThreadingTCPServer, ForkingTCPServer
        a pre-allocated pool of worker threads and process with nonthreaded server.
            Thread(target=server.serve_forever)
    `socket` lib to implement server.
        methods:
            server: 
                __init__, bind, listen
                accept, recv, send
            client:
                __init__, connect, send, recv
                
11.3. Creating UDP Server(A unreliable connection)
    you want to implement server that communicates with clients using UDP internet protocol.
    
    `socketserver` lib:
    a handler method class:
        BaseRequestHandler, StreamRequestHandler.
        server:
            UDPServer, ThreadingUDPServer, ForkingUDPServer
    `socket` lib to implement UDP server.
        server:
            __init__, bind
            recvfrom, sendto
        client:
            __init__, sendto, recvfrom
11.5 Create a simple REST-Based server.
    you want to be able to interact with your programs over the network using a simple
    REST-Based interface. However, you don't want to do it by installing a full-fledged 
    web programming framework.
    
    create a tiny library based on `WSGI` standard.
    
    Define wsgi application:
        function: 
            wsgi(environ, start_response)
        class:
            __init__(self):
                self.pathmap={} #  a dictionary that mappings(method, path) pairs to handler function.
            __call__(self):
                ...
        
    requirements:
        the returned result must be encoded into byte strings.
        
    create a simple server.
        from wsgiref.simple_server import make_server
    make serer create the underlying socket server.
    
11.6 Implementing a simple remote procedure with XML-RPC
    You want an easy way to execute functions and methods in Python program running on remote machines.
    
    1.create a server instance(SimpleXMLRPCServer)
    2.use `register_function`
    3.launch it with serve_forever() method
    4.client access the service: create a ServerProxy instance
"""