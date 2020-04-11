def isCongruentNumber(number):
    # a - b = k * n
    # b = 3
    # k = 4
    # number - 3 = 4 * n
    if((number - 3) % 4 == 0):
        return True
    else:
        return False
