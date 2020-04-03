import math


class Heap:
    def __init__(self):
        self.heapContainer = []

    def getLeftChildIndex(self, parentIndex):
        return (2 * parentIndex) + 1

    def getRightChildIndex(self, parentIndex):
        return (2 * parentIndex) + 2

    def getParentIndex(self, childIndex):
        return math.floor((childIndex + 1)/2) - 1

    def getLeftChild(self, parentIndex):
        return self.heapContainer[self.getLeftChildIndex(parentIndex)]

    def getRightChild(self, parentIndex):
        return self.heapContainer[self.getRightChildIndex(parentIndex)]

    def getParent(self, childIndex):
        return self.heapContainer[self.getParentIndex(childIndex)]

    def hasLeftChild(self, parentIndex):
        return self.getLeftChildIndex(parentIndex) < len(self.heapContainer)

    def hasRightChild(self, parentIndex):
        return self.getRightChildIndex(parentIndex) < len(self.heapContainer)

    def hasParent(self, childIndex):
        return self.getParentIndex(childIndex) >= 0

    def peek(self):
        return self.heapContainer[0]

    def poll(self):
        heapLength = len(self.heapContainer)
        if(heapLength == 0):
            return None
        elif(heapLength == 1):
            return self.heapContainer.pop()
        else:
            item = self.heapContainer[0]
            self.heapContainer[0] = self.heapContainer.pop()
            self.heapifyDown()
            return item

    def swap(self, index1, index2):
        temp = self.heapContainer[index1]
        self.heapContainer[index1] = self.heapContainer[index2]
        self.heapContainer[index2] = temp

    def add(self, item):
        self.heapContainer.append(item)
        self.heapifyUp()

    def heapifyUp(self):
        pass

    def heapifyDown(self):
        pass
