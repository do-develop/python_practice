class Solution:
    def lenLongestFibSubseq(self, arr: List[int]) -> int:
        nums = set(arr)
        res = 2
        for i in range(len(arr)):
            for j in range(i + 1, len(arr)):
                a, b, length = arr[i], arr[j], 2
                while a + b in nums:
                    a, b, length = b, a + b, length + 1
                    res = max(res, length)
        return res if res > 2 else 0
