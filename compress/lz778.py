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

#Decodes code word encoded with LZ77
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

#Computes noteboob and encoded string in LZ78 fashion
def lz78_encoding(omega):
    code_book = ds.CodeBook()
    n = len(omega)
    i = 0
    j = 0
    string = ""
    enc_string = []
    while(i < n):
        string += omega[i]
        if(code_book.hasWord(string)):
            i+= 1
        else:
            code_book.insert(string, j)
            enc_string.append(j)
            string = ""
            j+= 1
            i += 1
    return(enc_string, code_book)

#Decodes encoded string with LZ78 notebook
def lz78_decoding(eta, code_book):
    omega = ""
    for key in eta:
        omega += code_book.getWord(key)
    return omega

#Computes encoded string based on Lempel-Ziv-Welch coding notebook
def lzw_encoding(omega):
    omega += '$'
    code_book = ds.CodeBook()
    j = 256
    for i in range(j):
        code_book.insert(chr(i), i)
    string = ""
    enc_string = []
    n = len(omega)
    i = 0
    while(i < n):
        string +=  omega[i]
        msg_byte = omega[i+1]
        if(msg_byte == '$'):
            enc_string.append(code_book.getBinary(string))
            break
        look_up = string + msg_byte
        if(code_book.hasWord(look_up)):
            i += 1
        else:
            code_book.insert(look_up, j)
            j += 1
            enc_string.append(code_book.getBinary(string))
            string = ""
            i += 1
    return enc_string


#Decodes encoded word based on Lempel-Ziv-Welch coding
def lzw_decoding(eta):
    omega = ""
    code_book = ds.CodeBook()
    j = 256
    for i in range(j):
        code_book.insert(chr(i), i)
    n = len(eta)
    code = eta[0]
    string = code_book.getWord(code)
    omega += string
    i = 1
    while(i < n):
        code = eta[i]
        if(not(code_book.hasBinary(code))):
            entry = string + string[0]
        else:
            entry = code_book.getWord(code)
        omega += entry
        code_book.insert(string + entry[0],j)
        string = entry
        j += 1
        i += 1
    return omega
