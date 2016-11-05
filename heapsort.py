'''@author : https://github.com/Harnek'''

import random

"""Ascending sorting using MaxHeap Data Structure"""

class HeapSort:

    def __init__(self, a = []):
        self.a = a
        self.size = len(self.a)
        '''Build Heap if argument is an array'''
        if self.size:
            self.BuildMaxHeap()
        self.Sort()

    """Fix Heapify Property Downwards"""
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

    """Removes and Returns Max"""
    def extract_max(self):
        if self.size:
            self.a[0], self.a[self.size-1] = self.a[self.size-1], self.a[0]
            self.size -= 1
            self.MaxHeapifyDown(0)
        return False      

    def Sort(self):
        for i in range(self.size):
            self.extract_max()

    """Returns index of parent"""
    def parent(self, i):
        return (i-1)//2    

    """Returns index of left child"""
    def left(self, i):
        return 2*i + 1

    """Returns index of right child"""
    def right(self, i):
        return 2*i + 2

if __name__ == "__main__":
    ls = [random.randint(1, 100) for i in range(20)]
    HeapSort(ls)
    print(ls)