class Solution:
    def minSumOfLengths(self, arr: List[int], target: int) -> int:
        best_till = [math.inf] * len(arr) # min length subarray at certain index
        best = math.inf
        curr_sum = left = 0

        for right in range(len(arr)):
            curr_sum += arr[right]
            while curr_sum > target and left <= right:
                curr_sum -= arr[left]
                left += 1

            if curr_sum == target: # found new best
                best = min(best, best_till[left-1] + right - left + 1)
                best_till[right] = min(best_till[right-1], right - left + 1)
            else: # best we've seen is the previous best
                best_till[right] = best_till[right - 1] 
        
        if best == math.inf:
            return -1
        return best
