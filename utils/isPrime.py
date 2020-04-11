def isPrime(number):
    if number == 1 or number == 2 or number == 3:
        return True
    if number == 4:
        return False

    index = 3
    while number > index:
        if number % index == 0:
            return False
        else:
            index += 1

    if(index == number):
        return True
