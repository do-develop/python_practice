class Solution:
    def minimalKSum(self, nums: List[int], k: int) -> int:
        ans = k * (k + 1) // 2
        next_mini = k + 1

        for x in sorted(set(nums)):
            if x < next_mini:
                ans -= x
                ans += next_mini
                next_mini += 1
        return ans
