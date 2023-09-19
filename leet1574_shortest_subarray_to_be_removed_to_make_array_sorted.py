class Solution:
    def findLengthOfShortestSubarray(self, arr: List[int]) -> int:
        l, r = 0, len(arr) - 1
        while l < r and arr[l+1] >= arr[l]:
            l += 1
        if l == len(arr) - 1: # strictly increasing
            return 0 
        while r > 0 and arr[r-1] <= arr[r]:
            r -= 1
        to_remove = min(len(arr) - l - 1, r) # soley a prefix or soley a suffix

        # try to merge 2 sorted arrays
        for idx in range(l + 1):
            if arr[idx] <= arr[r]:
                to_remove = min(to_remove, r - idx - 1)
            elif r < len(arr) - 1:
                r += 1
            else:
                break
        return to_remove
        
