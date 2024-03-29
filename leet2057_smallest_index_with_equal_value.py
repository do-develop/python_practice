class Solution:
    def smallestEqual(self, nums: List[int]) -> int:
        candidates = []
        for i in range(len(nums)):
            if i % 10 == nums[i]:
                candidates.append(i)
        
        if len(candidates) > 0:
            return min(candidates)
        return -1
