class RSA:
    def __init__(self, p, q):
        d, e, n = self.createCryptoSystem(p, q)
        self.d = d
        self.e = e
        self.n = n

    def gcd(self, a, b):
        if b == 0:
            return a
        else:
            return self.gcd(b, a % b)

    def encrypt(self, m):
        c = pow(m, self.e)
        c = c % self.n
        return c

    def decrypt(self, c):
        m = pow(c, self.d)
        m = m % self.n
        return m

    def createCryptoSystem(self, p, q):
        n = p*q
        t = (p-1)*(q-1)

        for e in range(2, t):
            if self.gcd(e, t) == 1:
                break
        for i in range(1, 10):
            x = 1 + i*t
            if x % e == 0:
                d = int(x/e)
                break
        return d, e, n
