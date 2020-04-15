from BBS import BBS
from Tests import Tests

bits = BBS(7, 11).generateBits(20000)

print('bits1: ', bits)
print('bits1: ', Tests().series(bits))
