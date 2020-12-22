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
