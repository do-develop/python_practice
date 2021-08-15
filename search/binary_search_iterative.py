# Binary Search Iterative Version
def binary_search(arr, number):
    low = 0;
    high = len(arr) - 1
    mid = 0

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] < number:
            low = mid + 1

        elif arr[mid] > number:
            high = mid - 1

        else:
            return mid
    # if reached here, element not found from the array
    return -1

# Test iterative binary search
arr = [1, 3, 5, 7, 9, 11, 12]
num_to_find = 15

result = binary_search(arr, num_to_find)

if result != -1:
    print("Element is present at index ", str(result))
else:
    print("Element not found from the array")