'''
Implementation of the Huffman coding.
'''

import cla_util as util
import datastructures as ds

#Encoding procedure for binary huffman codes
def huffman_coding(omega):
    n = len(omega)
    q = ds.Heap()
    alphabet = util.word_alphabet(omega)
    dict = util.dictionary(alphabet)
    bits = [""]*len(alphabet)
    word_count = util.letter_count(omega, dict, alphabet)
    word_prob = [count / n for count in word_count]
    for i in range(len(word_prob)):
        q.insert([word_prob[i], i])
    #Encode least probable characters with one further bit
    while(q.size > 1):
        min1 = q.getMin()
        q.extractMin()
        min2 = q.getMin()
        q.extractMin()
        min2[0] += min1[0]
        #Add 0 to characters in set 2
        for i in range(1, len(min2)):
            bits[min2[i]] += "0"
        #ADD 1 to characters in set 1
        for i in range(1, len(min1)):
            min2.append(min1[i])
            bits[min1[i]] += "1"
        q.insert(min2)
        #Create code book based on encoding
        code_words = ds.CodeBook()
        for i in range (len(bits)):
            code = bits[i][::-1]
            code_words.insert(i, code)
    return(code_words)

#Compress word based on codebook
def huffman_compress(omega, code_book):
    binary_code = ""
    for letter in omega:
        binary_code += code_book.getBinary(letter)
    return(binary_code)

#Decompress code based on codebook
def huffman_decompress(eta, code_book):
    n = len(eta)
    current_word = ""
    omega = []
    for bit in eta:
        current_word += bit
        if(code_book.hasBinary(current_word)):
            omega.append(code_book.getWord(current_word))
            current_word = ""
    return(omega)
