class Tests:

    def singleBit(self, bits):
        minValue = 9725
        maxValue = 10275
        countBit1 = 0

        for bit in bits:
            if(bit == 1):
                countBit1 += 1

        if(countBit1 > minValue and countBit1 < maxValue):
            print('True. The sum of ones in a row is equal', countBit1)
            return True
        else:
            print('False. The sum of ones in a row is equal', countBit1)
            return False

    def series(self, bits):
        index = 0
        nextIndex = 1
        longestSeries = 0
        currentSeries = 1
        value = bits[0]
        breakSeries = False

        for i in bits:
            if(nextIndex < len(bits)):

                if(value is bits[nextIndex]):
                    currentSeries += 1
                    if(currentSeries > longestSeries):
                        longestSeries = currentSeries
                        value = i

                if(value is not bits[nextIndex]):
                    currentSeries = 1
                    value = bits[nextIndex]

            index += 1
            nextIndex += 1

        return {'longestSeries': longestSeries, 'value': value}
