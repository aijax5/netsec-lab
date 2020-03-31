import socket
import sys
import pickle
from bisect import bisect_left
from random import uniform
from RSA import RSA

HOST = '127.0.0.1'
PORT = 8019

m1 = 39


def setPrimes(primes):
    N = 10000
    temp = [0] * (N+1)
    for i in range(2, N+1):
        if (temp[i] == 0):
            temp[i] = i
            primes.append(i)
        j = 0
        while j < len(primes) and primes[j] <= temp[i] and i*primes[j] <= N:
            temp[i * primes[j]] = primes[j]
            j += 1


def randomPrime(p):
    primes = []
    if not primes:
        setPrimes(primes)
    prime = primes[:bisect_left(primes, p)]
    return prime[int(uniform(0, len(prime)))]


def aliceComputation(x, rsa):
    global m1
    while not m1 or m1 == 2:
        m1 = randomPrime(rsa.n)
    c = rsa.encrypt(m1)
    c1 = (c - x) % rsa.n
    print("calculated c1 : ",c1 ," m1 : ",m1)
    return c1, m1

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


def sendData(c1, x, m1):
    sock = socket.socket()
    sock.connect((HOST, PORT))
    data = aliceConfig(user="alice", data=c1, m1=m1)
    serializedData = pickle.dumps(data)
    sock.send(serializedData)
    while True:
        data_stream = sock.recv(1024)
        if data_stream:
            data = pickle.loads(data_stream)
            z = data.z
            P = data.p
            res = not z[x-1] % P == m1 % P
            data = aliceConfig(user="alice", res=res)
            if res:
                print("Alice is wealthier than Bob' ")
            else:
                print("Bob's wealthier than Alice")
                
            serializedData = pickle.dumps(data)
            sock.send(serializedData)


if __name__ == "__main__":
    x = int(input("enter Alice'sock Wealth(x) "))
    rsa = RSA(11, 5)
    c1, m1 = aliceComputation(x, rsa)
    sendData(c1, x, m1)
