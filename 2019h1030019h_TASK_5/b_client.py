import socket
import sys
import pickle
from bisect import bisect_left
from random import uniform
from RSA import RSA

HOST = '127.0.0.1'
PORT = 8019

rsa = RSA(11, 5)


class aliceConfig(object):
    """docstring for User"""

    def __init__(self, user=None, data=None, cmd=None, rsa=None, p=None, z=None, res=None, m1=None):
        self.user = user
        self.cmd = cmd
        self.value = data
        self.rsa = rsa
        self.p = p
        self.z = z
        self.res = res
        self.m1 = m1



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


def bobComputation(c1, m1, y, xr):
    m2 = []
    for i in range(1, xr+1):
        m = rsa.decrypt((c1+i) % rsa.n)
        m2.append(m)

    check = False
    checked = set()
    p = None
    while not check:
        while not p or p in checked:
            p = randomPrime(m1)
            # print(p)
        checked.add(p)
        z = []
        for _m2 in m2:
            z.append(_m2 % p)
        check = True

        for i, z1 in enumerate(z):
            if z1 == 0 or z1 >= p-1:
                continue
            for j, z2 in enumerate(z):
                if i == j or z2 == 0 or z2 >= p-1:
                    continue
                check = check and abs(z1-z2) >= 2

        if not check:
            p = None
    temp = []
    for i, _z in enumerate(z):
        if i >= y:
            temp.append(_z+1)
        else:
            temp.append(_z)

    return temp, p


def bobCommunication(y, xr):
    sock = socket.socket()
    data = aliceConfig(user="bob")
    data_string = pickle.dumps(data)

    sock.connect((HOST, PORT))

    sock.send(data_string)
    flag = True
    while True:
        data_stream = sock.recv(1024)
        if data_stream:
            data = pickle.loads(data_stream)
            if data.res != None:
                if data.res:
                   print("Alice is wealthier than Bob' ")
                else:
                    print("Bob's wealthier than Alice")
                
            if flag == True:
                c1 = data.value
                m1 = data.m1
                z, p = bobComputation(c1, m1, y, xr)
                data = aliceConfig(z=z, p=p)
                data_string = pickle.dumps(data)
                sock.send(data_string)
                flag = False


if __name__ == '__main__':
    y = int(input("bob'sock Wealth (y)<=10 : "))
    xr = 10
    bobCommunication(y, xr)
