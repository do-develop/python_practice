def binary_search(array, start, end):
    if start > end:
        return None
    mid = (start + end) //2

    if array[mid] == mid:
        return mid
    elif array[mid] > mid:
        return binary_search(array, start, mid - 1)
    else:
        return binary_search(array, mid + 1, end)

# GET USER INPUT
size = int(input())
array = list(map(int, input().split()))

# Perform binary search
index = binary_search(array, 0, size -1)

if index == 0:
    print(-1)
else:
    print(index)
