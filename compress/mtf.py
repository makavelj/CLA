'''
An implementation of the move to front algorithm.
'''

import copy


#Move to front encoding algorithm
def MTF_encode(omega, Lambda):
    n = len(omega)
    eta = []
    alphabet = copy.deepcopy(Lambda)
    #encode next character based on alphabet
    for w in omega:
        i = alphabet.index(w)
        eta.append(i)
        k = w
        #update alphabet in moving last character to the front of the alphabet
        for j in range(i+1):
            l = alphabet[j]
            alphabet[j] = k
            k = l
    return eta

#Move to front decoding algorithm
def MTF_decode(eta, Lambda):
    n = len(eta)
    omega = ""
    alphabet = copy.deepcopy(Lambda)
    #decode next character based on alphabet
    for i in range(n):
        omega += alphabet[eta[i]]
        k = alphabet[eta[i]]
        #update alphabet in moving last character to the front of the alphabet
        for j in range(eta[i]+1):
            l = alphabet[j]
            alphabet[j] = k
            k = l
    return omega
