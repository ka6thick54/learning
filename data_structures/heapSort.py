from minHeap import MinHeap
from maxHeap import MaxHeap


class AscHeapSort(MinHeap):

    def __init__(self, inputArray):
        super().__init__()
        for item in inputArray:
            self.add(item)

    def sort(self):
        print('***** Heapsort Ascending *****')
        print('Before sorting :::', self.heapContainer)
        sortedArray = []
        while (len(self.heapContainer)):
            sortedArray.append(self.poll())
        self.heapContainer = sortedArray
        print('After sorting :::', self.heapContainer)


ascHeapSort = AscHeapSort([87, 45, 47, 12, 68])
ascHeapSort.sort()


class DescHeapSort(MaxHeap):

    def __init__(self, inputArray):
        super().__init__()
        for item in inputArray:
            self.add(item)

    def sort(self):
        print('***** Heapsort Descending *****')
        print('Before sorting :::', self.heapContainer)
        sortedArray = []
        while (len(self.heapContainer)):
            sortedArray.append(self.poll())
        self.heapContainer = sortedArray
        print('After sorting :::', self.heapContainer)


descHeapSort = DescHeapSort([87, 45, 47, 12, 68])
descHeapSort.sort()
