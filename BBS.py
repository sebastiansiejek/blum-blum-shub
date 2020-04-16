from random import randint, getrandbits
from utils.isPrime import isPrime
from utils.isCongruentNumber import isCongruentNumber
from utils.coprime import coprime


class BBS:
    p = 0
    q = 0
    n = 0
    seed = 0
    generatedValues = []

    def __init__(self, p, q):
        self.setP(p)
        self.setQ(q)
        self.__setN()
        self.__setSeed()

    def setP(self, p):
        self.p = p

    def setQ(self, q):
        self.q = q

    def __setN(self):
        self.n = self.p * self.q

    def __setSeed(self):
        while(not coprime(self.n, self.seed) and self.seed < 1):
            self.seed = randint(1, self.n - 1)

    def __generateValue(self):
        x = 1
        while (coprime(self.n, x) and self.n >= 1):
            x = randint(0, self.n)
        powX = pow(x, 2)
        return powX % self.n

    def generateBits(self, amount):
        if(self.p == self.q):
            print('p should be diffrent than q')
            return False

        if (self.n == 0):
            print('N is equal 0')
            return False

        else:
            array = []
            amount += 1

            for i in range(amount):
                generatedValue = self.__generateValue()
                self.generatedValues.append(generatedValue)

                if(generatedValue % 2 == 0):
                    array.append(0)
                else:
                    array.append(1)

            return array
