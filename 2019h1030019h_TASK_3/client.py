from socket import AF_INET, socket, SOCK_STREAM
from threading import Thread
import hashlib

def hashString(msg):
    return hashlib.sha256(msg.encode()).hexdigest()

def main():
    while True:
        try:
            msg = sock.recv(BuffSize).decode("utf8")
            if(msg[0] == '0'):
                print("server: ", msg[1:])
            else:
                if msg[0] == '9':
                    print("server: ", msg[1:])
                    exit(0)
                if msg[0] == '2':
                    print("server: ", msg)
                    pswd = input()
                    sock.send(hashString(pswd).encode("utf8"))
                    input("\nregistered sucessfully\nPress Enter to exit...")
                    exit(0)
                else:
                    print("server: ", msg)
                    ip = input("your reply: ")
                    sock.send(ip.encode("utf8"))

        except OSError:
            break
        
if(__name__ == "__main__"):
    HOST = "127.0.0.1"
    PORT = 8008
    BuffSize = 1024
    ADDR = (HOST, PORT)
    sock = socket(AF_INET, SOCK_STREAM)
    sock.connect(ADDR)
    main()