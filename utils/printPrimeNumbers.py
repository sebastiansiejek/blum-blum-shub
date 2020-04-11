from utils.isPrime import isPrime


def printPrimeNumbers(max):
    for number in range(2, max):
        if(isPrime(number)):
            print(number)
