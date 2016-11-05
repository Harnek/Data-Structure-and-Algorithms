#author : harnek

class MaxHeap(object):

    """initiallize"""
    def __init__(self):
        self.array = []
        self.size = -1

    """Fix Tree going upwards when new element is inserted"""
    def reheapUp(self):
        i = self.size
        parent = (i-1)//2
        while i > 0 and self.array[i] > self.array[parent]:
            self.array[i], self.array[parent] = self.array[parent], self.array[i]
            i = parent
            parent = (i-1)//2   

    """Fix Tree going upwards when new element is inserted"""
    def reheapDown(self):
        i = 0
        while (2*i)+1 <= self.size:
            j = (2*i)+1
            if j+1 <= self.size and self.array[j] < self.array[j+1]:
                j += 1
            if self.array[i] < self.array[j]:
                self.array[i], self.array[j] = self.array[j], self.array[i]
                i = j
            else:
                break

    """insert at last pos and fix its position using reheapUp"""
    def insert(self, item):
        self.size += 1
        self.array.append(item)
        self.reheapUp()


    """removes and returns max element"""
    def extract(self):
        if self.size > 0:
            a = self.array[0]
            self.array[0], self.array[self.size] = self.array[self.size], self.array[0]
            self.size -= 1
            self.reheapDown()
            return self.array.pop()
        else:
            return -1

    def height(self):
        h = i = 0
        while i <= self.size and self.array[i]:
            h += 1
            i = (2*i) + 1
        return h

    def __repr__(self):
        #print(self.array)
        a = ""
        i = 0
        rchild = 0
        while i <= self.size:
            a += str(self.array[i]) + " "
            if i == rchild:
                a += "\n"
                rchild = (i*2)+2
            i += 1
        a += "\n"
        return a

if __name__ == "__main__":
    h = MaxHeap()
    h.insert(12)
    h.insert(13)
    h.insert(9)
    print(h)
    print(h.height())