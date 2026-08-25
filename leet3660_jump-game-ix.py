class Solution:
    def maxValue(self, nums: List[int]) -> List[int]:
        N = len(nums)
        result = [0] * N

        # (block_max, block_start, block_end)
        blocks = []

        for i in range(N):
            block_max = nums[i]
            block_start = i
            block_end = i

            while blocks and blocks[-1][0] > nums[i]:
                prev_max, prev_start, _prev_end = blocks.pop()
                block_max = max(block_max, prev_max)
                block_start = prev_start # extend left

            blocks.append((block_max, block_start, block_end))

        for block_max, block_start, block_end in blocks:
            for idx in range(block_start, block_end + 1):
                result[idx] = block_max
        
        return result
