import socket
import math
import random

def check_prime(p):
    isprime = 1 # assume p is prime 
    for i in range(2, p//2+1): 
        if p % i == 0:
            isprime = 0 # not a prime as i divides p 
            break
    if isprime==1:
        return 1 # True
    return 0 # False

def client_program():
    host = socket.gethostname()  # as both code is running on same pc
    port = 50000  # socket server port number

    client_socket = socket.socket()  # instantiate
    client_socket.connect((host, port))  # connect to the server
    
    # send message
    print("Wnat to 1.encrypt or 2.decrypt")
    n=int(input())
    if(n==1):
        encrypt(client_socket,n)
    else:
        decrypt(client_socket)
    

def encrypt(client_socket,n):
    client_socket.send(str(n).encode())
    print("encrypt data")
    pub_str=client_socket.recv(1024).decode()
    list = pub_str.split (",")
    Msg1=39
    C=math.pow(Msg1,int(list[0]))%int(list[1])
    #x=random.randint(1,10)
    x=4
    C1=C-x
    size_x=math.log(x,2)
    size=int(math.floor(size_x))
    send_list=str(C1)+","+str(size)
    client_socket.send(send_list.encode())
    recv_data=client_socket.recv(4096).decode()
    print("received data",recv_data)
    list = recv_data.split (",")
    val1=int(math.floor(float(list[x-1])))
    val2=int(list[-1])
    if(val1%val2 != x):
        print("x > y")
    else:
        print("x < y")
    
    client_socket.close()  # close the connection


def decrypt(client_socket):
    val=client_socket.recv(1024).decode()
    print("decrypt data ")
    public_key=7
    N=55
    pub_key=str(public_key)+","+str(N)
    pri_bob=23
    print("Decrypt",pub_key)
    client_socket.send(pub_key.encode())
    data_cipher=client_socket.recv(1024).decode()
    list = data_cipher.split (",")
    #y=random.randint(1,10)
    y=2
    C1=float(list[0])
    size=int(list[1])
    size=math.pow(2,size)
    size=math.floor(size)
    M2=[]
    for i in range(1,101):
        M2.insert(i-1,(math.pow(C1+i,pri_bob))%N)
    print("M2",M2)
    print("Choosing a large prime less than size_x")
    for p in range(size,2,-1):
        if check_prime(p) == 1:
            flag=0
            Zu=[]
            for i in range(1,101):
                Zu.insert(i-1,(M2[i-1])%p)
            for i in range(0,100):
                for j in range(i+1,100):
                    x=Zu[i]-Zu[j]
                    print(x)
                    if((x>=2 or x<=-2)==False):
                        flag=1
                        break
                if(flag==0):
                    print(Zu) 
                    if((Zu[i]>0 and Zu[i]<(p-1))==False):
                        flag=1
                        break
                if(flag==1):
                    break
            if(flag==0):
                break          
    Z=[]
    for i in range(0,100):
        if(i<=y):
            Z.insert(i,Zu[i])
        else:
            Z.insert(i,Zu[i]+1)
    print(Z)
    str1=","
    Z.append(p)
    listToStr = ','.join(map(str, Z)) 
    #print("listToStr",listToStr)
    client_socket.send(listToStr.encode())
    client_socket.close()

if __name__ == '__main__':
    client_program()