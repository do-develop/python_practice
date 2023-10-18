class Solution:
    def waysToMakeFair(self, nums: List[int]) -> int:
        evens, odds = sum(nums[0::2]), sum(nums[1::2])
        ways = cur_even = cur_odd = 0

        for i, n in enumerate(nums):
            if i % 2 == 0:
                evens -= n
                ways += (cur_even + odds == cur_odd + evens)
                cur_even += n
            else:
                odds -= n
                ways += (cur_even + odds == cur_odd + evens)
                cur_odd += n
        return ways
