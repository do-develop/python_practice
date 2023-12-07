class Solution:
    def countNicePairs(self, nums: List[int]) -> int:
        # x + rev(y) == y + rev(x) can be rewritten as:
        # x - rev(x) == y - rev(y)
        def rev(num):
            result = 0
            while num:
                result = result * 10 + num % 10
                num //= 10
            return result
        # to find x - rev(x) == y - rev(y)
        # store x - rev(x)
        arr = []
        for i in range(len(nums)):
            arr.append(nums[i] - rev(nums[i]))
        
        dic = defaultdict(int)
        ans = 0
        MOD = 10 ** 9 + 7
        for n in arr:
            ans = (ans + dic[n]) % MOD
            dic[n] += 1
        return ans

