from random import randint
from utils.isPrime import isPrime
from utils.isCongruentNumber import isCongruentNumber
from utils.coprime import coprime


def findX(p, q):
    if(isPrime(p) and isCongruentNumber(p) and isPrime(q) and isCongruentNumber(q)):
        n = p * q
        x = 1
        while (coprime(n, x)):
            x = randint(0, n)
        return x
