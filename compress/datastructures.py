'''
Implementation of useful datastructures:
Suffix Array
MinHeap
CodeBook
'''

MAX = 999999999999999999999999999

#Creates of Suffix Array
def SuffixArray(omega):
    SA =sorted(range(len(omega)), key=lambda i: omega[i:])
    return(SA)

#Heap Datastructure for priority queues
class Heap():
    def __init__(self, type='min'):
        self.heap = []
        self.size = 0
        self.type = type
    def getType(self):
        assert(self.type == 'min' or self.type == 'max'), ('Heap type is either max or min')
        return self.type
    #Return Min Value of the list
    def getMin(self):
        assert(self.getType() is 'min'), ('For min value a heap with type min should be used')
        return self.heap[0]
    #Return Max Value of the list
    def getMax(self):
        assert(self.getType() is 'max'), ('For max value a heap with type max should be used')
        return self.heap[0]
    #Extracs Min Value of the list and rebuild heap
    def extractMin(self):
        assert(self.getType() is 'min'), ('For min extraction a heap with type min should be used')
        self.heap[0] = self.heap[self.size-1]
        self.heap[self.size-1] = [MAX]
        self.downheap(0)
    #Extract Max Value of the list and rebuild heap
    def extractMax(self):
        assert(self.getType() is 'max'), ('For max extraction a heap with type max should be used')
        self.heap[0] = self.heap[self.size-1]
        self.heap[self.size-1] = [-1*MAX]
        self.downheap(0)
    #Insert new Element and rebuild heap
    def insert(self, node):
        self.heap.append(node)
        self.size += 1
        return self.upheap(self.size-1)
    #Rebuild heap by swapping with parent
    def upheap(self, i):
        heap_type = self.getType()
        parent = int((i-1)/2)
        #Case for MinHeap: Move element upwards until parent is smaller
        if(heap_type is 'min'):
            #Check with father and swap unitl heap property is satisfied
            if(self.heap[i] < self.heap[parent]):
                flag = self.heap[i]
                self.heap[i] = self.heap[parent]
                self.heap[parent] = flag
                return(self.upheap(parent))
            else: return self.heap
        #Case for MaxHeap: Move element upwards until parent is greater
        else:
            #Check with father and swap unitl heap property is satisfied
            if(self.heap[i] > self.heap[parent]):
                flag = self.heap[i]
                self.heap[i] = self.heap[parent]
                self.heap[parent] = flag
                return(self.upheap(parent))
            else: return self.heap
    #Rebuild heap by swapping with children
    def downheap(self, i):
        heap_type = self.getType()
        if(self.size < 2*(i+1)+1):
            del self.heap[self.size-1]
            self.size -= 1
            return self.heap
        #Case for MinHeap: Move element downwards until children are greater
        if(heap_type is 'min'):
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
                del self.heap[self.size-1]
                self.size -= 1
                return self.heap
        #Case for MaxHeap: Move element downwards until children are smaller
        else:
            greaterChild = max(self.heap[2*(i+1)-1], self.heap[2*(i+1)])
            #Check which of the two children is smaller and swap until heap property is satisfied
            if(self.heap[2*(i+1)-1] == greaterChild): maxChild = 2*(i+1)-1
            else: maxChild = 2*(i+1)
            if(self.heap[i] < self.heap[maxChild]):
                flag = self.heap[i]
                self.heap[i] = self.heap[maxChild]
                self.heap[minChild] = flag
                return(self.downheap(maxChild))
            else:
                del self.heap[self.size-1]
                self.size -= 1
                return self.heap

#Code book implementing a biderctional dictionary
class CodeBook():
    def __init__(self):
        self.bits_word = {}
        self.word_bits = {}
    #Insert word and responding binary code
    def insert(self, word, binary):
        self.bits_word[binary] = word
        self.word_bits[word] = binary
    #Returns the binary code word for the letter
    def getBinary(self, word):
        return self.word_bits[word]
    #Returns the letter corresponding to the binary code word
    def getWord(self, bits):
        return self.bits_word[bits]
    #Check if code book contatins this binary code
    def hasBinary(self, bits):
        if bits in self.bits_word: return True
        else: return False
    #Check if code book contains this letter
    def hasWord(self, word):
        if word in self.word_bits: return True
        else: return False
    #To print information of the code book
    def getCode_book(self):
        return(self.bits_word, self.word_bits)
