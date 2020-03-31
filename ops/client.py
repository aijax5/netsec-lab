import socket
import math
import random

def isPrime(p):
    isprime = 1 
    for i in range(2, p//2+1): 
        if p % i == 0:
            isprime = 0 
            break
    if isprime==1:
        return True
    return False


def encrypt( conn,n):
    conn.send(str(n).encode())
    print("encrypt data")
    PUKY= conn.recv(1024).decode()
    print("received keys, ")
    e,n = PUKY.split (",")
    m1=39
    C=math.pow(m1,int(e))%int(n)
    x=4
    c1=C-x
    size_x=math.log(x,2)
    size=int(math.floor(size_x))
    send_list=str(c1)+","+str(size)
    conn.send(send_list.encode())
    recv_data= conn.recv(4096).decode()
    print("received data",recv_data)
    list = recv_data.split (",")
    val1=int(math.floor(float(list[x-1])))
    val2=int(list[-1])
    if(val1%val2 != x):
        print("x > y")
    else:
        print("x < y")
    
    conn.close()  


def decrypt(conn):
    val= conn.recv(1024).decode()
    PUKY=7
    n=55
    pub_key=str(PUKY)+","+str(n)
    d=23
    print("Decrypt",pub_key)
    conn.send(pub_key.encode())
    data_cipher= conn.recv(1024).decode()
    list = data_cipher.split (",")
    y=2
    c1=float(list[0])
    size=int(list[1])
    size=math.pow(2,size)
    size=math.floor(size)
    m2=[]
    for i in range(1,101):
        m2.insert(i-1,(math.pow(c1+i,d))%n)
    print("m2",m2)
    for p in range(size,2,-1):
        if isPrime(p) == 1:
            flag=0
            temp=[]
            for i in range(1,101):
                temp.insert(i-1,(m2[i-1])%p)
            for i in range(0,100):
                for j in range(i+1,100):
                    x=temp[i]-temp[j]
                    print(x)
                    if((x>=2 or x<=-2)==False):
                        flag=1
                        break
                if(flag==0):
                    print(temp) 
                    if((temp[i]>0 and temp[i]<(p-1))==False):
                        flag=1
                        break
                if(flag==1):
                    break
            if(flag==0):
                break          
    z=[]
    for i in range(0,100):
        if(i<=y):
            z.insert(i,temp[i])
        else:
            z.insert(i,temp[i]+1)
    print(z)
    str1=","
    z.append(p)
    listToStr = ','.join(map(str, z)) 
    print("listToStr",listToStr)
    conn.send(listToStr.encode())
    conn.close()

if __name__ == '__main__':
    host = socket.gethostname()  
    port = 8051  
    conn = socket.socket()  
    conn.connect((host, port)) 
    
    n=int(input("Menu\n1.Encrypt\n2.Decrypt\nChoose an option: "))
    if(n==1):
        encrypt( conn,n)
    else:
        decrypt( conn)
    