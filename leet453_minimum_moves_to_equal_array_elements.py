class Solution:
    def minMoves(self, nums: List[int]) -> int:
        """
        # brute force (time exceeds)

        count = 0 # movement count
        while True:
            big, small = max(nums), min(nums)
            if big == small: # all numbers are equal
                break
            
            diff = big - small
            idx, count = nums.index(big), count + diff
            for i in range(len(nums)):
                nums[i] = nums[i] + diff if i != idx else nums[i]
        return count
        """
        # how many decrement needed to make current min
        # totle movemnet = current sum - all equal to min state
        return sum(nums) - len(nums) * min(nums)
