import socket
import pickle
from threading import Thread


HOST = '127.0.0.1'
PORT = 8019
Thcount = 0
data = []
key = {}
password = {}
users = []

class aliceConfig(object):
    def __init__(self, user=None, data=None, cmd=None, rsa=None, p=None, z=None, res=None, m1=None):
        self.user = user
        self.cmd = cmd
        self.value = data
        self.rsa = rsa
        self.p = p
        self.z = z
        self.res = res
        self.m1 = m1



def connBob(conn):
    user = None
    with conn:
        while True:
            data_stream = conn.recv(1024)
            if data_stream:
                data = pickle.loads(data_stream)
                user = data.user
                if data.value or data.z:
                    print("ewe")
                    data_string = pickle.dumps(data)
                    users[0].send(data_string)


def connAlice(conn):
    with conn:
        while True:
            user = None
            data_stream = conn.recv(1024)
            if data_stream:
                data = pickle.loads(data_stream)
                data_string = pickle.dumps(data)
                users[1].send(data_string)


if __name__ =="__main__":
    print("server is up and running")
    connectedUsers = 0
    with socket.socket() as s:
        s.bind((HOST, PORT))
        s.listen()
        while True:
            conn, addr = s.accept()
            if(len(users) == 2):
                users = []
            users.append(conn)
            connectedUsers += 1
            if connectedUsers == 2:
                print("both alice and bob are connected!")
                aliceThread = Thread(target=connAlice, args=(users[0],))
                bobThread = Thread(target =connBob,args= (users[1],))
                aliceThread.start()
                bobThread.start()
                aliceThread.join()
                bobThread.join()