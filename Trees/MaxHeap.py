'''@author : https://github.com/Harnek

Implementation of Max Heap (complete binary tree data structure)

Complexity:
            Average   Worst case
    Space   O(n)      O(n)
    Search  O(n)      O(n)
    Insert  O(1)      O(log n)
    Delete  O(log n)  O(log n)
    Peek    O(1)      O(1)

Parent (i-1)/2
Left   (2*i)+1
Right  (2*i)+2
'''

class MaxHeap:

    def __init__(self, a = []):
        self.a = a
        self.size = len(self.a)
        '''Build Heap if argument is an array'''
        if self.size:
            self.BuildMaxHeap()

    """Fix Heapify Property going upwards"""
    def MaxHeapifyDown(self, i):
        j = self.left(i)
        while j < self.size:
            if j+1 < self.size and self.a[j] < self.a[j+1]:
                j += 1
            if self.a[i] < self.a[j]:
                self.a[i], self.a[j] = self.a[j], self.a[i]
                i = j
                j = self.left(i)
            else:
                break
        """Recursive Implementation"""
        # largest = i
        # l = self.Left(i)
        # r = self.Right(i)
        # if l < self.size and self.a[l] > self.a[i]:
        #     largest = l
        # if r < self.size and self.a[r] > self.a[largest]:
        #     largest = r
        # if largest != i:
        #     self.a[i], self.a[largest] = self.a[largest], self.a[i]
        #     self.MaxHeapifyDown(largest)

    """Fix Heapify Property going upwards"""
    def MaxHeapifyUP(self, i):
        p = self.parent(i)
        while i > 0 and self.a[i] > self.a[p]:
            self.a[i], self.a[p] = self.a[p], self.a[i]
            i = p
            p = self.parent(i)

    """insert new element at the end and heapifyUp"""
    def insert(self, item):
        self.size += 1
        self.a.append(item)
        self.MaxHeapifyUP(self.size-1)

    """Build Max Heap From Array"""
    def BuildMaxHeap(self):
        for i in range(self.size//2, -1, -1):
            self.MaxHeapifyDown(i)    

    """Returns Max"""
    def maxx(self):
        if self.a:
            return self.a[0]
        return False

    """Removes and Returns Max"""
    def extract_max(self):
        if self.size:
            temp = self.a[0]
            self.size -= 1
            self.a[0] = self.a[self.size]
            self.a.pop()
            self.MaxHeapifyDown(0)
            return temp
        return False

    """returns height of tree"""
    def height(self):
        h = i = 0
        while i <= self.size and self.array[i]:
            h += 1
            i = (2*i) + 1
        return h        

    """Returns index of parent"""
    def parent(self, i):
        return (i-1)//2    

    """Returns index of left child"""
    def left(self, i):
        return 2*i + 1

    """Returns index of right child"""
    def right(self, i):
        return 2*i + 2

    def __len__(self):
        return self.size

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

import random

if __name__ == "__main__":
    ls = [random.randint(1, 100) for i in range(20)]
    print(ls)
    h = MaxHeap(ls)
    print(h)
