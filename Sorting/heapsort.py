'''@author : https://github.com/Harnek
Implementation of HeapSort
Complexity:
    Heapify()   O(log n)
    BuildHeap() O(n)
    HeapSort()  O(nLogn)
'''

'''Iterative'''
def heapify1(A, idx, maxidx):
    left = 2*idx + 1
    right = 2*idx + 2
    largest = idx
    while left < maxidx:
        if left < maxidx and A[left] > A[idx]:
            largest = left
        if right < maxidx and A[right] > A[largest]:
            largest = right
        if largest != idx and A[idx] < A[largest]:
            A[idx], A[largest] = A[largest], A[idx]
            idx = largest
            left = 2*idx + 1
            right = 2*idx + 2
        else:
            break

'''Recursive'''
def heapify(A, idx, maxidx):
    left = 2*idx + 1
    right = 2*idx + 2
    largest = idx
    if left < maxidx and A[left] > A[idx]:
        largest = left
    if right < maxidx and A[right] > A[largest]:
        largest = right
    if largest != idx:
        A[idx], A[largest] = A[largest], A[idx]
        heapify(A, largest, maxidx)

'''Build Heap'''
def buildHeap(A):
    n = len(A)
    for i in range(n//2-1, -1, -1):
        heapify(A, i, n)

'''HeapSort'''
def heapSort(A):
    buildHeap(A)
    for i in range(len(A)-1, 0, -1):
        A[0], A[i] = A[i], A[0]
        heapify(A, 0, i)

if __name__ == "__main__":
    a = list(range(15))
    heapSort(a)
    print(a)