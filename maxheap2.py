'''@author : Harnek'''

"""
-------+-------++---------+
Indexed|   1   ||    0    |
-------+-------++---------+
Parent | i/2   || (i-1)/2 |
Left   | 2*i   || (2*i)+1 |
Right  | 2*i+1 || (2*i)+2 |
-------+-------++---------+
"""

class MaxHeap():

    def __init__(self, a = []):
        self.a = a
        self.size = len(self.a)
        '''Build Heap if argument is an array'''
        if self.size:
            self.BuildMaxHeap()

    """Fix Heapify Property going upwards"""
    def MaxHeapifyDown(self, i):
        largest = i
        l = self.Left(i)
        r = self.Right(i)
        if l < self.size and self.a[l] > self.a[i]:
            largest = l
        if r < self.size and self.a[r] > self.a[largest]:
            largest = r
        if largest != i:
            self.a[i], self.a[largest] = self.a[largest], self.a[i]
            self.MaxHeapifyDown(largest)

    """Fix Heapify Property going upwards"""
    def MaxHeapifyUP():
        pass

    """insert new element at the end and heapifyUp"""
    def insert(self, item):
        self.size += 1
        self.a.append(item)
        self.MaxHeapifyUP()

    """Build Max Heap From Array"""
    def BuildMaxHeap(self):
        for i in range(self.size//2, -1, -1):
            self.MaxHeapifyDown(i)    

    """Returns Max"""
    def maxi(self):
        if self.a:
            return self.a[0]
        return False

    """Removes and Returns Max"""
    def extract_maxi(self):
        if self.size:
            temp = self.a[0]
            self.size -= 1
            self.a[0] = self.a[self.size]
            self.a.pop()
            self.MaxHeapifyDown(0)
            return temp
        return False

    """Returns index of parent"""
    def Parent(self, i):
        return (i-1)//2    

    """Returns index of left child"""
    def Left(self, i):
        return 2*i + 1

    """Returns index of right child"""
    def Right(self, i):
        return 2*i + 2


    """Print Representation
             1
         /'''  '''\
        2          3
      /''\       /''\
     4    5     6    7
    / \  / \   / \   / \
    8 9 10 11 12 13 14 15
    """
    def __repr__(self):
        p = ""
        i = 0
        rchild = 0
        while i < self.size:
            p += str(self.a[i]) + " "
            if i == rchild:
                p += "\n"
                rchild = 2*i+2
            i += 1
        return p

if __name__ == "__main__":
    ls = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
    h = MaxHeap(ls)
    print(h)