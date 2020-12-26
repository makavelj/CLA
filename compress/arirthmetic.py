'''
Implementation of the Shannon-Fano-Elias Coding and real arithmetic coding.
'''

import math
import util
import datastructures as ds

#Plain Shannon Fano Elias coding, less efficient than Huffman
def shannon_fano_elias_coding(omega):
    n = len(omega)
    alphabet = util.word_alphabet(omega)
    m = len(alphabet)
    dict = util.dictionary(alphabet)
    bits = ""
    word_count = util.letter_count(omega, dict, alphabet)
    word_prob = [count / n for count in word_count]
    sum = 0
    notebook = ds.CodeBook()
    for i in range(m):
        prob = word_prob[i]
        sum += prob
        Fx = sum - 0.5*prob
        bits = util.decimal2binary(Fx)
        bits = bits[2:len(bits)]
        encoding_length = math.ceil(math.log(1/prob, 2)) + 1
        while(len(bits) < encoding_length):
            bits += '0'
        if(len(bits) > encoding_length):
            bits = bits[0:encoding_length]
        notebook.insert(alphabet[i], bits)
    return notebook
