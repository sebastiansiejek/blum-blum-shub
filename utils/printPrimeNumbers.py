from utils.isPrime import isPrime
from utils.isCongruentNumber import isCongruentNumber


def printPrimeNumbers(max):
    for number in range(2, max):
        if(isPrime(number)):
            print(number)


def printPrimeAndCongruentNumbers(max):
    for number in range(2, max):
        if(isPrime(number) and isCongruentNumber(number)):
            print(number)
