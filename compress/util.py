'''
General util functions for compression.
'''

import random

#Compute integer values for a word
def word_to_int(omega):
    set = []
    for c in omega:
        set.append(ord(c))
    return set

#Creates string based on integers
def int_to_word(A):
    string = ""
    for e in A:
        string += chr(e)
    return string

#Randomized quicksort implementation with list comprehension
def quicksort(A):
    if len(A) <= 1: return A

    pivotindex = random.randint(0, len(A)-1)
    pivot = A[pivotindex]

    equal = [x for x in A if x == pivot]
    lesser = [x for x in A if x < pivot]
    greater = [x for x in A if x > pivot]

    return quicksort(lesser) + equal + quicksort(greater)

#Create list of the alphabet for a word
def word_alphabet(omega):
    dict = {}
    alphabet = []
    j = 0
    for c in omega:
        if(not(c in dict)):
            dict[c] = j
            j += 1
            alphabet.append(c)
    return(alphabet)

#Create dictionary to access index in array
def dictionary(alphabet):
    dict = {}
    i = 0
    for letter in alphabet:
        dict[letter] = i
        i += 1
    return(dict)

#Compute the number of occurences of every letter
def letter_count(omega, sigma=False, alphabet=False):
    n = len(omega)
    #If no alphabet table availabe create one one on the fly
    if(alphabet==False):
        alphabet = word_alphabet(omega)
        alphabet = sorted(alphabet)
    #If no dictionary availabe to access index create one on the fly
    if(sigma==False): sigma = dictionary(alphabet)
    count = [0]*len(alphabet)
    for i in range(n):
        letter = sigma[omega[i]]
        count[letter] +=1
    return count

#Compute all Cyclic shifts
def cyclic_shifts(factors):
    rotations = []
    m = len(factors)
    for i in range(m):
        concat = factors[i] + factors[i]
        n = len(factors[i])
        for j in range(n):
            rotations.append(concat[j:j+n])
    return rotations
