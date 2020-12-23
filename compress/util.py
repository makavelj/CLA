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
def letter_count(omega, sigma=None, alphabet=None):
    n = len(omega)
    #If no alphabet table availabe create one one on the fly
    if(alphabet==None):
        alphabet = word_alphabet(omega)
        alphabet = sorted(alphabet)
    #If no dictionary availabe to access index create one on the fly
    if(sigma==None): sigma = dictionary(alphabet)
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

#Min Heap Datastructure for priority queues
class MinHeap():
    def __init__(self):
        self.heap = []
        self.size = 0
    #Return Min Value of the list
    def getMin(self):
        return self.heap[0]
    #Extracs Min Value of the list and rebuild heap
    def extractMin(self):
        self.heap[0] = self.heap[self.size-1]
        del self.heap[self.size-1]
        self.size -= 1
        self.downheap(0)
    #Insert new Element and rebuild heap
    def insert(self, node):
        self.heap.append(node)
        self.size += 1
        return self.upheap(self.size-1)
    #Rebuild heap by swapping with parent
    def upheap(self, i):
        parent = int((i-1)/2)
        #Check with father and swap unitl heap property is satisfied
        if(self.heap[i] < self.heap[parent]):
            flag = self.heap[i]
            self.heap[i] = self.heap[parent]
            self.heap[parent] = flag
            return(self.upheap(parent))
        else: return self.heap
    #Rebuild heap by swapping with children
    def downheap(self, i):
        if(self.size < 2*(i+1)+1):
            return self.heap
        smallerChild = min(self.heap[2*(i+1)-1], self.heap[2*(i+1)])
        #Check which of the two children is smaller and swap until heap property is satisfied
        if(self.heap[2*(i+1)-1] == smallerChild): minChild = 2*(i+1)-1
        else: minChild = 2*(i+1)
        if(self.heap[i] > self.heap[minChild]):
            flag = self.heap[i]
            self.heap[i] = self.heap[minChild]
            self.heap[minChild] = flag
            return(self.downheap(minChild))
        else:
            return self.heap
