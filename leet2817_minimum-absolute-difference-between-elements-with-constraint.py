class Solution:
    def minAbsoluteDifference(self, nums: List[int], x: int) -> int:
        if x == 0:
            return 0

        candidates = SortedList([])
        bestDiff = float('inf')

        for i in range(x, len(nums)):
            candidates.add(nums[i - x])
            curr = nums[i]

            index = candidates.bisect_left(curr)
            if index < len(candidates):
                bestDiff = min(bestDiff, abs(candidates[index] - curr))
            if index > 0:
                bestDiff = min(bestDiff, abs(candidates[index - 1] - curr))
        return bestDiff
