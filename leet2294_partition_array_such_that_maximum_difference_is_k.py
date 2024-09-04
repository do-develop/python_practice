class Solution:
    def partitionArray(self, nums: List[int], k: int) -> int:
        nums.sort()
        partition = 1

        mn = mx = nums[0]
        for n in nums:
            mn = min(mn, n)
            mx = max(mx, n)
            if mx - mn > k:
                partition += 1
                mx = mn = n # start new subsequence with n as the first element
        return partition
