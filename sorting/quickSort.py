class QuickSort:

    def sort(self, arrayToSort, low, high):
        if(low < high):
            pivot = self.quick(arrayToSort, low, high)
            self.sort(arrayToSort, low, pivot-1)
            self.sort(arrayToSort, pivot + 1, high)
        return arrayToSort

    def quick(self, arrayToSort, low, high):
        i = low - 1
        pivot = arrayToSort[high]
        for j in range(low, high):
            if(arrayToSort[j] < pivot):
                i += 1
                arrayToSort[i], arrayToSort[j] = arrayToSort[j], arrayToSort[i]
        arrayToSort[i+1], arrayToSort[high] = arrayToSort[high], arrayToSort[i+1]
        return i + 1


inputArray = [8, 7, 6, 5, 4, 3, 2, 1]
quickSort = QuickSort()
print("::::::::: Quick Sort :::::::::")
print("Before Sorting ::: ", inputArray)
print("After Sorting ::: ", quickSort.sort(inputArray, 0, 7))
print("Best Time complexity ::: O(n log n)")
print("Worst Time complexity ::: O(n2)")
print("Space complexity ::: O(log n)")
