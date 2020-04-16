class Tests:

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
