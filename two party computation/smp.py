import sys
import random
from RSA import RSA
from RSA import Utilities
from datetime import datetime
xr =4
class Alice:
    def __init__(self,x,keys):
        self.x = x
        self.rsa = RSA(keys)
        self.util = Utilities()
        

    def computation(self,bobKey,m1):
        self.m1 = m1
        self.c = self.rsa.encrypt(self.m1,PUKY=bobKey)
        self.c1 = self.c - self.x
        return self.c1
    
    def generateResults(self,z,p):
        if z[self.x ]%p == self.m1 % p :
            print("Bob's value is greater than Alice's")
            return False
        print("Value of Alice is greater than Bob's")
        return True
    

class Bob:
    def __init__(self,y,keys):
        self.y = y
        self.rsa = RSA(keys)
        self.util = Utilities()

    def computation(self,c1,m1,p):
        m2 = list()
        for i in range(xr+1):
            if i ==0:
                m2.append(-1)
                continue
            m2.append(self.rsa.decrypt(c1+i))
        self.m2 = m2
        count = 1
        random.seed(datetime.now())   
        while count != 0:
            count = 0

            # self.p = random.randrange(2,m1)
            # # print("fermat ka  p",self.p)
            # while(not self.util.isPrime(self.p )):
            #     self.p = random.randrange(2,m1)
            #     # print(self.p,"loppa")
            # print("set p as" ,self.p)
            self.p =p
            # input("p ki toh")
            z= list(range(xr+1))
            for i in range(1,xr+1):
                z[i] = self.m2[i] %self.p 
            for i in range(1,xr+1):
                for j in range(1,xr+1):
                    if(abs(z[i]-z[j]) < 2 and i!=j ):
                        print(i , " ",j )
                        count += 1
                        input("enter to contuneue")
                        break         
                if count >0:
                    break
            print(z)

        self.z = z
        print(z,"!!!done..")
        # self.p = p
        for i in range(1,xr+1):
            if i>y:
                self.z[i] = self.z[i]+1
        return (self.z,self.p)
               
    def getZ(self):
        return self.z

    def getResult(self, response):
        if response:
            print("Value of Alice is greater than Bob's")
        else:
            print("Bob's value is greater than Alice's")

if __name__ == "__main__":

    n = int(input("enter value of n at bob : "))
    e = int(input("enter bob's Publckey(e) : "))
    d = int(input("enter bob's private key : "))
    m1 = int(input("enter value of m1: "))
    p = int(input("enter value of prime p for bob's computaion : "))
    print("Enter two distinct integers x,y 1<= x,y <= 4 seperated by space: ")
    x = input().split(' ')
    y = int(x[1])
    x = int(x[0])
  
    keys = ((e,n),d)
    alice = Alice(x,keys)
    bob = Bob(y,keys)
    
    c1 = alice.computation(bob.rsa.getPublicKey(),m1)
    print("got c1 as ",c1," m1 as ",m1)
    z,p = bob.computation(c1,m1,p)
    response = alice.generateResults(z,p)
    bob.getResult(response)