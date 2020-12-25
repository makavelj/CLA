'''
Implementation of the Lempel Ziv Encodings.
'''

import datastructures as ds
import util


#Computes LZ77 standard encoding
def lz77_encoding(omega):
    jump_length = []
    m = 0
    n = len(omega)
    jump_length.append([0, 0, omega[0]])
    i = 0
    while(i < n-1):
        search = True
        pattern = ""
        matches = []
        i += 1
        j = i
        #look up the largest string in preceding substring
        while(search == True):
            pattern += omega[i]
            substring = omega[0:i]
            final_matching = matches
            matches = util.knuth_morris_pratt(substring, pattern)
            if(matches == []):
                search = False
                if(len(pattern) == 1):
                    jump_length.append([0, 0, omega[i]])
                else:
                    jumps = j - max(final_matching)
                    l = len(pattern)-1
                    jump_length.append([jumps, l, omega[i]])
            else:
                i += 1
    return jump_length

#Encodes code word encoded with LZ77
def lz77_decoding(jump_length):
    omega = ""
    for tripple in jump_length:
        j = tripple[0]
        l = tripple[1]
        c = tripple[2]
        n = len(omega)
        for i in range(l):
            omega += omega[n-j]
            n += 1
        omega += c
    return omega
