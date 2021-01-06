'''
Implementation of the Shannon-Fano-Elias Coding and Real Arithmetic Coding.
'''

import math
import cla_util as util
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

def real_arithmetic_coding(omega, word):
        n = len(omega)
        alphabet = util.word_alphabet(omega)
        m = len(alphabet)
        dict = util.dictionary(alphabet)
        word_count = util.letter_count(omega, dict, alphabet)
        word_prob = [count / n for count in word_count]
        prob_ranges = []
        prob_sum = 0
        for i in range(m):
            start = prob_sum
            prob_sum += word_prob[i]
            prob_ranges.append([start, prob_sum])
        for j in range(len(word)-1):
            index = dict[word[j]]
            low = prob_ranges[index][0]
            high = prob_ranges[index][1]
            prob = high - low
            prob_sum = low
            prob_ranges = []
            for i in range(m):
                start = prob_sum
                prob_sum += word_prob[i] * prob
                prob_ranges.append([start, prob_sum])
        last_letter = word[len(word)-1]
        last_letter_index = dict[last_letter]
        final_range = prob_ranges[last_letter_index]
        bits_low = util.decimal2binary(final_range[0])
        bits_high = util.decimal2binary(final_range[1])
        return bits_low, bits_high



low, high = (real_arithmetic_coding("aabbbbbccc", "bac"))
print(low, high)
