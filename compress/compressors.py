'''
Using the implemented algorithms for compression procedures
'''

import bwt
import mtf
import huffman as huf

#Compression based on Bijective BWT, MTF and Huffman encoding
def bijective_huffman_compress(omega):
    string_bwt = bwt.BBWT(omega)
    string_mtf, alphabet = mtf.MTF_encode(string_bwt)
    code_book = huf.huffman_coding(string_mtf)
    binary = huf.huffman_compress(string_mtf, code_book)
    return(binary, code_book, alphabet)

#Decompression for algorithm based on Bijective BWT, MTF and Huffman encoding
def bijective_huffman_decompress(binary, notebook, alphabet):
    string_mtf = huf.huffman_decompress(binary, notebook)
    string_bwt = mtf.MTF_decode(string_mtf, alphabet)
    omega = bwt.BBWT_inv(string_bwt)
    return(omega)

#Compression based on plain BWT, MTF and Huffman encoding
def bwt_huffman_compress(omega):
    string_bwt = bwt.BWT(omega)
    string_mtf, alphabet = mtf.MTF_encode(string_bwt)
    code_book = huf.huffman_coding(string_mtf)
    binary = huf.huffman_compress(string_mtf, code_book)
    return(binary, code_book, alphabet)

#Decompression for algorithm based on Bijective BWT, MTF and Huffman encoding
def bwt_huffman_decompress(binary, notebook, alphabet):
    string_mtf = huf.huffman_decompress(binary, notebook)
    string_bwt = mtf.MTF_decode(string_mtf, alphabet)
    omega = bwt.BWT_inv(string_bwt)
    return(omega)
