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
        
12. Creating TCP Server (A reliable connection)
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
                
13. Creating UDP Server(A unreliable connection)
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
"""