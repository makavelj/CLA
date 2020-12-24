'''
Test file for compressing algorithms
'''

import compressors as cp
import random
import string

def test_bwt_huffman_compress(string):
    bin, note, alph = cp.bwt_huffman_compress(string)
    string_re = cp.bwt_huffman_decompress(bin, note, alph)
    assert(string == string_re)

def test_bijective_huffman_compress(string):
    bin, note, alph = cp.bijective_huffman_compress(string)
    string_re = cp.bijective_huffman_decompress(bin, note, alph)
    assert(string == string_re)

if __name__ == '__main__':
    n = random.randrange(100000)
    string =''.join(random.choices(string.ascii_uppercase + string.digits, k = n))
    test_bwt_huffman_compress(string)
    test_bijective_huffman_compress(string)
