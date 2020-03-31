#!/usr/bin/python           # This is server.py file                                                                                                                                                                           

import socket 
import sys              # Import socket module
list_conn=dict()
from _thread import *
__all__ = ("error", "LockType", "start_new_thread", "interrupt_main", "exit", "allocate_lock", "get_ident", "stack_size", "acquire", "release", "locked")


def on_new_client(clientsocket,addr):
    while True:
        print("waiting for msg")
        msg = clientsocket.recv(1024)
        #do some checks and if msg == someWeirdSignal: break:
        print(addr, ' >> ', msg)
        print("from connected user: " + str(msg))
        for x,y in list_conn.items():
            if(x!=addr):
                clientsocket1=y
                y.send(msg)
        #msg = input('SERVER >> ')
        #Maybe some code to compute the last digit of PI, play game or anything else can go here and when you are done.
        #clientsocket.send(msg.encode())
    clientsocket.close()

s = socket.socket()         # Create a socket object
host = socket.gethostname() # Get local machine name
port = 50000                # Reserve a port for your service.

print('Server started!')
print('Waiting for clients...')

s.bind((host, port))        # Bind to the port
s.listen(5)                 # Now wait for client connection.

while True:
   c, addr = s.accept()
        # Establish connection with client.
   print('Got connection from', addr)
   list_conn.update({addr:c})
   start_new_thread(on_new_client,(c,addr))
   #Note it's (addr,) not (addr) because second parameter is a tuple
   #Edit: (c,addr)
   #that's how you pass arguments to functions when creating new threads using thread module.
s.close()