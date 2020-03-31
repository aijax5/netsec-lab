from socket import AF_INET, socket, SOCK_STREAM
from threading import Thread
from time import sleep
keys = {}
# users = {}
delay = 0.1
HOST = "127.0.0.1"
PORT = 8018
BuffSize = 1024
ADDR = (HOST,PORT)
SOCK = socket(AF_INET, SOCK_STREAM)
SOCK.bind(ADDR)

def connectClients():
    while True:
        client, client_address = SOCK.accept()
        print("%s:%s has connected." % client_address)
        # client.send("0Hello there! Let's get you registered! ".encode("utf8"))
        uid = client.recv(BuffSize).decode("utf8")
        Thread(target=registerUser, args=(client,uid)).start()

def printTable():
    for user in keys:
        print(user," --> ",keys[user])

def registerUser(conn,uid):
    def updatePUKY(uid):
        # parent conn
        e = conn.recv(BuffSize).decode()
        ph = conn.recv(BuffSize).decode()
        keys[uid] = (int(e),int(ph))

    def getPUKY():
        query = conn.recv(BuffSize).decode()
        print( "trying to fetch key of ",query)
        if query in keys:
            e,ph = keys[query]
            conn.send("1".encode())
            sleep(delay)
            conn.send(str(e).encode())
            sleep(delay)
            conn.send(str(ph).encode())
        else:
            conn.send("0".encode())

    print(uid)
    while True:
        cmd = conn.recv(BuffSize).decode("utf8")
        print("cmd : ",cmd)
        if cmd == "upkey":
            updatePUKY(uid)
            printTable()
        if cmd == "gkey":
            getPUKY()
        if cmd == "x":
            break
    return
   
    
if __name__ == "__main__":

    SOCK.listen(5)
    print("server is up and running...")
    t = Thread(target=connectClients)
    t.start()  
    t.join()
    SOCK.close()