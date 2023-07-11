class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        # binary search approach

        def find_division_sum(divisor: int) -> int:
            total = 0
            for n in nums:
                total += ceil((1.0 * n) / divisor)
            return total

        ans = -1
        lo, hi = 1, max(nums)

        while lo <= hi:
            mid = (lo + hi) // 2
            result = find_division_sum(mid)

            if result <= threshold:
                ans = mid
                hi = mid - 1 # still look for minimum result
            else:
                lo = mid + 1
        
        return ans
