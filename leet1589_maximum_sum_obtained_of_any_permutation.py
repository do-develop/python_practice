class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        mod = 10 ** 9 + 7
        n = len(nums)
        counts = [0] * (n + 1)
        # request counts
        for a, b in requests:
            counts[a] += 1      # every index after this point will be counted 1 more time 
            counts[b + 1] -= 1  # every index after end will be counted 1 less time
        # get prefix sum of request counts
        for i in range(1, n):
            counts[i] += counts[i - 1]

        nums.sort()
        counts.pop()
        counts.sort()

        return sum(a * b for a, b in zip(nums, counts)) % mod
