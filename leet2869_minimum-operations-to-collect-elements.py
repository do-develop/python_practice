class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        N = len(nums)
        numSet, idx = set(), N - 1
        while len(numSet) < k:
            if nums[idx] <= k:
                numSet.add(nums[idx])
            idx -= 1

        return N - idx - 1
