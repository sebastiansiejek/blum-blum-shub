from random import randint
from utils.isPrime import isPrime
from utils.isCongruentNumber import isCongruentNumber
from utils.coprime import coprime


class BBS:
    p = 0
    q = 0
    s = 1
    n = 0
    x0 = 0
    random_sequence = []

    def __init__(self, p, q):
        self.p = p
        self.q = q
        if(isPrime(p) and isCongruentNumber(p) and isPrime(q) and isCongruentNumber(q)):
            self.__generateN()
            self.__calcS()
            self.__setOriginalGeneratorValue()
            self.__test()

    def __generateN(self):
        self.n = self.p * self.q

    def __calcS(self):
        while (coprime(self.n, self.s) and self.n >= 1):
            self.s = randint(0, self.n)

    def __setOriginalGeneratorValue(self):
        powX = pow(self.s, 2)
        self.x0 = powX % self.n

    def __test(self):
        print(self.s)
        for x in range(32):
            self.random_sequence.append((x ** 2) % self.x0)
