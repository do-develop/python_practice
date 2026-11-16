class Solution:
    def minOperations(self, nums: List[int]) -> int:
        count = 0
        seen = set()
        N = len(nums)

        duplicate_idx = -1

        for i in reversed(range(N)):
            if nums[i] in seen:
                duplicate_idx = i
                break
            else:
                seen.add(nums[i])
        return math.ceil((duplicate_idx+1)/3)