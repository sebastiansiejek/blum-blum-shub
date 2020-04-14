from random import randint, getrandbits
from utils.isPrime import isPrime
from utils.isCongruentNumber import isCongruentNumber
from utils.coprime import coprime


class BBS:
    p = 0
    q = 0
    n = 0

    def __init__(self, p, q):
        self.setP(p)
        self.setQ(q)
        if(isPrime(self.p) and isCongruentNumber(self.p) and isPrime(self.q) and isCongruentNumber(self.q)):
            self.__setN()

    def __setN(self):
        self.n = self.p * self.q

    def __generateValue(self):
        x = 1
        while (coprime(self.n, x) and self.n >= 1):
            x = randint(0, self.n)
        powX = pow(x, 2)
        return powX % self.n

    def setP(self, p):
        self.p = p

    def setQ(self, q):
        self.q = q

    def printBits(self, amount):
        array = []
        amount += 1
        for i in range(amount):
            if(self.__generateValue() % 2 == 0):
                array.append(0)
            else:
                array.append(1)
        return array
