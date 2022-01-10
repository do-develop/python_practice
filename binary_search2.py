"""
get element counts from a sorted array
"""
# without using bisect library
"""
def count_by_value(array, x):
    size =len(array)
    f = first(array, x, 0, size -1)

    if not f:
        return 0

    l = last(array, x, 0, size -1)

    return l - f + 1

def first(array, target, start, end):
    if start > end:
        return None
    mid = (start + end) // 2
    # left most index
    if (mid == 0 or target > array[mid-1]) and array[mid] == target:
        return mid
    elif array[mid] >= target:
        return first(array, target, start, mid - 1)
    else:
        return first(array, target, mid + 1, end)

def last(arry, target, start, end):
    if start > end:
        return None
    mid = (start + end) // 2
    # right most index
    if (mid == size-1 or target < array[mid + 1]) and array[mid] == target:
        return mid
    elif array[mid] > target:
        return last(array, target, start, mid - 1)
    else:
        return last(array, target, mid + 1, end)

size, target_val = map(int, input().split())
array = list(map(int, input().split()))
target_val_count = count_by_value(array, target_val)

if target_val_count == 0:
    print(-1)
else:
    print(target_val_count)
    
"""

from bisect import bisect_left, bisect_right

def count_by_range(array, left_value, right_value):
    right_index = bisect_right(array, right_value)
    left_index = bisect_left(array, left_value)
    return right_index - left_index

# get user input
size, target = map(int, input().split())
array = list(map(int, input().split()))

# get data count
count = count_by_range(array,target,target)

if count == 0:
    print(-1)
else:
    print(count)
