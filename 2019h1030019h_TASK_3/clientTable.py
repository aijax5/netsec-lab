from socket import AF_INET, socket, SOCK_STREAM
from threading import Thread

clients = {}
users = {}

HOST = "127.0.0.1"
PORT = 8008
BuffSize = 1024
ADDR = (HOST,PORT)
SOCK = socket(AF_INET, SOCK_STREAM)
SOCK.bind(ADDR)

def connectClients():
    while True:
        client, client_address = SOCK.accept()
        print("%s:%s has connected." % client_address)
        client.send("0Hello there! Let's get you registered! ".encode("utf8"))
        
        Thread(target=registerUser, args=(client,)).start()


def registerUser(conn):
    conn.send("Please enter 4 digit user ID".encode("utf8")) 
    uid = conn.recv(BuffSize).decode("utf8")
    if uid in users:
        print("user ID : %s has already registered",uid)
        conn.send(("9user ID : %s has already registered" % uid).encode())
        return
    msg2 = '2user ID : %s \nPlease enter a password:\n' % uid
    conn.send(bytes(msg2, "utf8"))
    pswd = conn.recv(BuffSize).decode("utf8")
    print(pswd)
    users[uid] = pswd
    clients[uid] = conn
    print("\n\n********** updated table of hashed passwords **********")
    for user in users:
        print(user," --> ",users[user])
    
if __name__ == "__main__":

    SOCK.listen(5)
    print("server is up and running...")
    t = Thread(target=connectClients)
    t.start()  
    t.join()
    SOCK.close()