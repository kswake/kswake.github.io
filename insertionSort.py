# simple insertion sort algorithm

def insertionSort(arr):
    # iterate from 1st to last element of arr
    for i in range(1, len(arr)):
        #store arr[i] as key to use for replacement later 
        key = arr[i]
        # need j to be i-1 for comparison purposes
        j = i - 1

        # move elements of the array to the 'left' until either we reach the left end of the array (j=0)
        # or until [key] is not >= arr[j] -> when no longer true, the array up to i will be sorted    
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j = j - 1
        arr[j + 1] = key
    return arr

# testing
arr = [213, 3, 453, 4, 512, 7, 43, 9, 12, 77, 66]
print("unsorted: ", arr)
arrSorted = insertionSort(arr)
print("unsorted: ", arrSorted)