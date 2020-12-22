'''
Tests for the Burrows Wheeler Transform
'''

import bwt

print(bwt.BWT("banana") == "annb$aa")
print(bwt.BWT_inv("annb$aa") == "banana")
