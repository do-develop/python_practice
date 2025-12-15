class Solution:
    def minOperations(self, nums: List[int]) -> int:
        flip_candidates = deque()
        ops = 0

        for i in range(len(nums)):
            while flip_candidates and i > flip_candidates[0] + 2:
                flip_candidates.popleft()
            
            if (nums[i] + len(flip_candidates)) % 2 == 0:
                if i + 2 >= len(nums):
                    return -1
                ops += 1
                flip_candidates.append(i)
        return ops
