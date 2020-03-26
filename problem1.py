# Problem statement: Find If the array has a pair of integers that sum to the value provided

# Brute force solution
def bruteForcePairExists(inputArray, sum):
    for i in range(len(inputArray)):
        for j in range(i+1, len(inputArray)):
            if inputArray[i]+inputArray[j] == sum:
                return True
    return False

print("-----Brute Force Approach-----")
print("Time complexity ::: O(n^2)")
print("Result :::", bruteForcePairExists([1,2,4,4],8))

# Best solution
def pairExists(inputArray, sum):
    complement = set()
    noOfIterations = 1
    for item in inputArray:
        comp = int(sum)-int(item)
        if item in complement:
            return True
        else:
            complement.add(int(comp))
        noOfIterations += 1
    print(complement)
    return False

# Time complexity O(n) explanation: We are using set as the time complexity of find an element in a set in constant O(1)
# and we iterate only once through the input array

print("-----Best Solution-----")
print("Time complexity ::: O(n)")
print("Result :::", pairExists([1,2,4,4],8))