from socket import AF_INET, socket, SOCK_STREAM
from threading import Thread
import hashlib
from RSA import RSA #importing  RSA class from RSA.py
from time import sleep
delay = 0.1
def hashString(msg):
    return hashlib.sha256(msg.encode()).hexdigest()

def updatePublicKey(uid,PUKY):
    sock.send("upkey".encode())
    sleep(delay)
    sock.send(str(PUKY[0]).encode())
    sleep(delay)
    sock.send(str(PUKY[1]).encode())

def getPublicKey(uid):
    sock.send("gkey".encode())
    sleep(delay)
    sock.send(uid.encode())
    sleep(delay)
    response = sock.recv(BuffSize).decode()
    if(response == "1"):
        e = sock.recv(BuffSize).decode()
        ph = sock.recv(BuffSize).decode()
        print("public key of %s is ( %s , %s)"%(uid,e,ph))
    if(response == '0'):
        print("QUERY NOT FOUND IN THE TABLE")


if __name__ == "__main__":
    HOST = "127.0.0.1"
    PORT = 8018
    BuffSize = 1024
    ADDR = (HOST, PORT)
    sock = socket(AF_INET, SOCK_STREAM)
    sock.connect(ADDR)
    r = RSA()

    uid = input("every client is uniquely identified with a user id\nEnter 4-digit user id: ")
    sock.send(uid.encode())
    sleep(delay)
    updatePublicKey(uid,r.getPublicKey())
    while True:
        cmd = int(input("MENU\n1. Update RSA\n2.Query a Public key\n3.Exit\nChoose a option: " ))
        if(cmd == 1):
            r= RSA()
            updatePublicKey(uid,r.getPublicKey())
        if(cmd == 2):
            query =  input("enter the uid the client who's Public key is to retrived: ")
            getPublicKey(query)
        if(cmd == 3):
            sock.send("x".encode())
            exit(0)