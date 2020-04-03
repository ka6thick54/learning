from heap import Heap


class MinHeap(Heap):

    def __init__(self):
        super().__init__()

    def heapifyUp(self):
        currentIndex = len(self.heapContainer) - 1
        while (self.hasParent(currentIndex)
               and self.heapContainer[currentIndex]
               < self.heapContainer[self.getParentIndex(currentIndex)]):
            parentIndex = self.getParentIndex(currentIndex)
            self.swap(currentIndex, parentIndex)
            currentIndex = parentIndex

    def heapifyDown(self):
        currentIndex = 0
        nextIndex = None
        while(self.hasLeftChild(currentIndex)):
            if(self.hasRightChild(currentIndex)
               and self.getLeftChild(currentIndex)
               > self.getRightChild(currentIndex)):
                nextIndex = self.getRightChildIndex(currentIndex)
            else:
                nextIndex = self.getLeftChildIndex(currentIndex)

            if(self.heapContainer[nextIndex]
                    < self.heapContainer[currentIndex]):
                self.swap(currentIndex, nextIndex)
            currentIndex = nextIndex
