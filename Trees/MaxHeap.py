'''
author : https://github.com/Harnek

Implementation of Max Heap (complete binary tree data structure)

Complexity:
            Average   Worst case
    Space   O(n)      O(n)
    Search  O(n)      O(n)
    Insert  O(1)      O(log n)
    Delete  O(log n)  O(log n)
    Peek    O(1)      O(1)
'''

class MaxHeap:

    def __init__(self, heapList = []):
        self.heapList = heapList
        self.size = len(self.heapList)
        '''Build Heap if argument is an array'''
        if self.size:
            self.buildHeap()

    """Fix Heapify Property going upwards"""
    def percDown(self, i):
        j = self.left(i)
        while j < self.size:
            if j+1 < self.size and self.heapList[j] < self.heapList[j+1]:
                j += 1
            if self.heapList[i] < self.heapList[j]:
                self.heapList[i], self.heapList[j] = self.heapList[j], self.heapList[i]
                i = j
                j = self.left(i)
            else:
                break
        """Recursive Implementation"""
        # largest = i
        # l = self.Left(i)
        # r = self.Right(i)
        # if l < self.size and self.heapList[l] > self.heapList[i]:
        #     largest = l
        # if r < self.size and self.heapList[r] > self.heapList[largest]:
        #     largest = r
        # if largest != i:
        #     self.heapList[i], self.heapList[largest] = self.heapList[largest], self.heapList[i]
        #     self.percDown(largest)

    """Fix Heapify Property going upwards"""
    def percUp(self, i):
        p = self.parent(i)
        while i > 0 and self.heapList[i] > self.heapList[p]:
            self.heapList[i], self.heapList[p] = self.heapList[p], self.heapList[i]
            i = p
            p = self.parent(i)

    """insert new element at the end and heapifyUp"""
    def insert(self, item):
        self.size += 1
        self.heapList.append(item)
        self.percUp(self.size-1)   

    """Removes and Returns Max"""
    def delMax(self):
        if self.size:
            temp = self.heapList[0]
            self.size -= 1
            self.heapList[0] = self.heapList[self.size]
            self.heapList.pop()
            self.percDown(0)
            return temp
        return False

    def buildHeap(self):
        for i in range(self.size//2, -1, -1):
            self.percDown(i)         

    def parent(self, i):
        return (i-1)//2    

    def left(self, i):
        return 2*i + 1

    def right(self, i):
        return 2*i + 2

    def __len__(self):
        return self.size

    def __repr__(self):
        p = ""
        i = 0
        rchild = 0
        while i < self.size:
            p += str(self.heapList[i]) + " "
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
