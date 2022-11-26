class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        # sort the array and find the median
        length = len(nums)
        mid = length // 2
        nums.sort()
        moves = 0
        # the absolute difference of the current number and the middle number is the number of moves
        for i in range(length):
            moves += abs(nums[i] - nums[mid])
        return moves
