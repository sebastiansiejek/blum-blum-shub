from random import randint
from utils.isPrime import isPrime
from utils.isCongruentNumber import isCongruentNumber
from utils.coprime import coprime


class BBS:
    p = 0
    q = 0
    x = 1
    n = 0

    def __init__(self, p, q):
        self.p = p
        self.q = q
        if(isPrime(p) and isCongruentNumber(p) and isPrime(q) and isCongruentNumber(q)):
            self.__calcX()

    def __calcX(self):
        self.n = self.p * self.q
        while (coprime(self.n, self.x)):
            self.x = randint(0, self.n)
