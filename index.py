from BBS import BBS
from Tests import Tests

bits = BBS(7, 31)
bits = bits.generateBits(20000)
print(Tests().series(bits))
print(Tests().singleBit(bits))
