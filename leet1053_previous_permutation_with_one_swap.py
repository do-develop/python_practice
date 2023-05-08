class Solution:
    def prevPermOpt1(self, arr: List[int]) -> List[int]:
        i = len(arr) - 2
        while i >= 0 and arr[i] <= arr[i + 1]:
            i -= 1
        if i >= 0:
            swap_point = i + 1
            for j in range(swap_point + 1, len(arr)):
                if arr[swap_point] < arr[j] < arr[i]:
                    swap_point = j
            arr[swap_point], arr[i] = arr[i], arr[swap_point]
        return arr
