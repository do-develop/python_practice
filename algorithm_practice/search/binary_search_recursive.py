# Recursive binary search

def binary_search(arr, low, high, x):

    # base case
    if high >= low:
        mid = (high + low) // 2

        if arr[mid] == x:
            return mid

        elif arr[mid] > x:
            return binary_search(arr, low, mid-1, x)

        else:
            return binary_search(arr, mid+1, high, x)

    else:
        # element is not found from the array
        return -1


# Test binary search
arr = [2, 3, 5, 7, 8, 10]
num_to_find = 1

result = binary_search(arr, 0, len(arr)-1, num_to_find)

if result != -1:
    print("Element is present at index", str(result))
else:
    print("Element is not found from the array")

