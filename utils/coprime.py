from math import gcd as bltin_gcd


def coprime(a, b):
    return bltin_gcd(a, b) == 1
