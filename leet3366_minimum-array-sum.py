class Solution:
    def minArraySum(self, nums: List[int], k: int, op1: int, op2: int) -> int:
        N = len(nums)

        @cache
        def dp(i, o1, o2):
            if i == N:
                return 0

            x = nums[i]

            # 1. No operation
            res = x + dp(i + 1, o1, o2)
            # 2. op1 
            if o1 > 0:
                res = min(res, (x + 1) // 2 + dp(i + 1, o1 - 1, o2))
            # 3. op2 — only if valid
            if o2 > 0 and x >= k:
                res = min(res, x - k + dp(i + 1, o1, o2 - 1))
            # 4. both operations
            if o1 > 0 and o2 > 0:
                # op1 → op2
                if (x + 1) // 2 >= k:
                    res = min(res, ((x + 1) // 2 - k) + dp(i + 1, o1 - 1, o2 - 1))
                # op2 → op1
                if x >= k:
                    res = min(res, (x - k + 1) // 2 + dp(i + 1, o1 - 1, o2 - 1))

            return res

        return dp(0, op1, op2)
