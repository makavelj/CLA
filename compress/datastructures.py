'''
Implementation of useful datastructures like Suffix Array etc.
'''

#Creates of Suffix Array
def SuffixArray(w):
    SA =sorted(range(len(w)), key=lambda i: w[i:])
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
