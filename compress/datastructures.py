'''
Implementation of useful datastructures like Suffix Array etc.
'''

MAX = 999999999999999999999999999

#Creates of Suffix Array
def SuffixArray(omega):
    SA =sorted(range(len(omega)), key=lambda i: omega[i:])
    return(SA)

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
        self.heap[self.size-1] = [MAX]
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
            del self.heap[self.size-1]
            self.size -= 1
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
            del self.heap[self.size-1]
            self.size -= 1
            return self.heap

#Code book implementing a biderctional dictionary
class code_book():
    def __init__(self):
        self.bits_word = {}
        self.word_bits = {}
    #Insert word and responding binary code
    def insert(self, word, binary):
        self.bits_word[binary] = word
        self.word_bits[word] = binary
    def getBinary(self, word):
        return self.word_bits[word]
    def getWord(self, bits):
        return self.bits_word[bits]
    def hasBinary(self, bits):
        if bits in self.bits_word: return True
        else: return False
    def hasWord(self, word):
        if word in self.word_bits: return True
        else: return False
    def getCode_book(self):
        return(self.bits_word, self.word_bits)
