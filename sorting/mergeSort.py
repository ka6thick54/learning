import math


class MergeSort:

    def sort(self, arrayToSort, low, high):
        if(low < high):
            mid = math.floor((low + high)/2)
            self.sort(arrayToSort, low, mid)
            self.sort(arrayToSort, mid+1, high)
            self.merge(arrayToSort, low, mid, high)
        return arrayToSort

    def merge(self, arrayToSort, low, mid, high):
        leftPart = arrayToSort[low: mid+1]
        rightPart = arrayToSort[mid+1:high+1]
        i = 0
        j = 0
        k = low
        m = len(leftPart)
        n = len(rightPart)
        while((i < m) and (j < n)):
            if(leftPart[i] < rightPart[j]):
                arrayToSort[k] = leftPart[i]
                k += 1
                i += 1
            else:
                arrayToSort[k] = rightPart[j]
                k += 1
                j += 1
        while(i < m):
            arrayToSort[k] = leftPart[i]
            k += 1
            i += 1
        while(j < n):
            arrayToSort[k] = rightPart[j]
            k += 1
            j += 1
        return arrayToSort


inputArray = [8, 7, 6, 5, 4, 3, 2, 1]
mergeSort = MergeSort()
print("Before Sorting ::: ", inputArray)
print("After Sorting ::: ", mergeSort.sort(inputArray, 0, 7))
print("Time complexity ::: O(n log n)")
print("Space complexity ::: O(n)")
