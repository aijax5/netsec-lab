import random

class Utilities:
    def fermatTest(self,p):
        a = random.randrange(1,p-1)
        if  (a**p - a)%p :
            return False
        return True
    
    def gcd(self,a,b):
        if (b == 0):
            return a
        else:
            return self.gcd(b, a % b)

    def euclidean_gcd(self,a,b):
        x, old_x = 0, 1
        y, old_y = 1, 0

        while (b != 0):
            q = a // b
            a, b = b, a - q * b
            old_x, x = x, old_x - q * x
            old_y, y = y, old_y - q * y

        return a, old_x, old_y

class RSA:

    def __init__(self):
        self.util = Utilities()
        self.createCrypoSystem()

    def setPrimes(self):
        self.p = random.randrange(5,50)
        while(not self.util.fermatTest(self.p)):
            self.p = random.randrange(2,50)
        
        self.q = random.randrange(10,50)
        while(self.q == self.p or not self.util.fermatTest(self.p)):
            self.q = random.randrange(10,50)

    
    def createCrypoSystem(self):
        
        self.setPrimes()
        self.n = self.p*self.q
        self.tot = (self.p -1)*(self.q-1)
        
        while (True):
            temp = random.randrange(2, self.tot)

            if (self.util.gcd(temp, self.tot) == 1):
                self.e = temp
                break
        # self.e = 7
        self.PU = (self.e,self.n)

        def getPrivateKey():
            gcd, x, y = self.util.euclidean_gcd(self.e, self.tot)
            return x%self.tot
        
        self.d = getPrivateKey()
        print("_____ created a RSA cryptosystem with following configuration _____")
        print("randomly choosen primes p = ",self.p," q = ",self.q)
        print("public key (e, phi(n)) = ",self.PU)
        print("private key d = ", self.d)

    def getPublicKey(self):
        print(self.PU)
        return self.PU

    def encrypt(self,PUKY = self.PU):
        m = int(input("Please enter a message (format: INT32 < "+str(self.n)+" )"))
        e = PUKY[0]
        n = PUKY[1]
        temp = e
        c =1
        while(temp):
            c = (c*m )
            c %= n
            temp -= 1
        c = c % n
        print("cipher text of message M = ",m," is C = ",c)
        return c

    def decrypt(self):
        c = int(input("Please enter a cipher (format: INT32 < "+str(self.n)+" )"))
        c= int(c)
        temp = self.d
        m =1
        while(temp):
            m = (c*m )
            m %= self.n
            temp -= 1
        m = m % self.n
        print("Plain text of cipher c = ",c," is m = ",m)
        
if __name__ =='__main__':
    rsa = RSA()
    while(True):
        print("----------------**** THE RSA API ****----------------")
        print("Select option\n1. Encrypt\n2. Decrpyt\n3. Get Public key of the CryptoSystem\n4. Exit \n")
        ip = int(input())
        if ip == 1:
            rsa.encrypt()
        if ip == 2:
            rsa.decrypt()
        if ip == 3:
            rsa.getPublicKey()
        if ip == 4:
            print("Thank You /\\")
            break