import socket 
import sys              
users={}
from _thread import *
__all__ = ("error", "LockType", "start_new_thread", "interrupt_main", "exit", "allocate_lock", "get_ident", "stack_size", "acquire", "release", "locked")


def clientHandler(conn,conn_addr):
    while True:
        print("waiting for msg")
        msg = conn.recv(1024)
        print("from connected user: " + str(msg))
        for x,y in users.items():
            if(x!=conn_addr):
                clientsocket1=y
                y.send(msg)
   
    conn.close()

sock = socket.socket()         
host = socket.gethostname() 
port = 8051               

print('server is up and running!')
sock.bind((host, port))        
sock.listen(5)                 

while True:
   c, conn_addr = sock.accept()
   print('new client  at', conn_addr)
   users.update({conn_addr:c})
   start_new_thread(clientHandler,(c,conn_addr))
sock.close()