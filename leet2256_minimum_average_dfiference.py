class Solution:
    def minimumAverageDifference(self, nums: List[int]) -> int:
        N = len(nums)
        total_nums = sum(nums)
        left_nums = 0
        min_diff = math.inf
        loc = 0

        for i, v in enumerate(nums):
            left_nums += v
            left_avg = left_nums // (i + 1)
            right_nums = total_nums - left_nums
            right_avg = right_nums // (N - i - 1) if (N - i - 1) != 0 else 0
            diff = abs(left_avg - right_avg)
            if min_diff > diff:
                min_diff = diff
                loc = i

        return loc
