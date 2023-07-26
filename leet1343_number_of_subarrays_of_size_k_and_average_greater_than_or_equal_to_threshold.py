class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        count = 0
        cur_sum = sum(arr[:k-1])
        left = 0
        for right in range(k-1, len(arr)):
            cur_sum += arr[right]
            if cur_sum // k >= threshold:
                count += 1
            cur_sum -= arr[left]
            left += 1
        return count
