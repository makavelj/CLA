'''
Tests for the Lempel Ziv Encodings
'''

import lz778 as lz
import random
import string

#Tests if LZ77 can decode a random encoded string correctly
def test_lzw(string):
    enc = lz.lzw_encoding(string)
    dec = lz.lzw_decoding(enc)
    assert(string == dec), ('LZW does decode encoded string not correctly')

#Tests if LZ77 can decode a random encoded string correctly
def test_77(string):
    enc = lz.lz77_encoding(string)
    dec = lz.lz77_decoding(enc)
    assert(string == dec), ('LZ77 does decode encoded string not correctly')

if __name__ == '__main__':
    n = random.randrange(10000)
    string =''.join(random.choices(string.ascii_uppercase + string.digits, k = n))
    test_lzw(string)
    test_77(string)
