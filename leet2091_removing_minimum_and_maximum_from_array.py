class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        # Three cases --> compare and do the one with minimum deletion
        N = len(nums)
        max_pos = nums.index(max(nums))
        min_pos = nums.index(min(nums))
        min_idx = min(min_pos, max_pos)
        max_idx = max(min_pos, max_pos)
        left_count = max_idx + 1
        right_count = N - min_idx
        both_count = N + min_idx - max_idx + 1
        
        return min(left_count, right_count, both_count)
