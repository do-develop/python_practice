class Solution:
    def maxGoodNumber(self, nums: List[int]) -> int:
        def compare(x, y):
            if x + y > y + x:
                return -1
            return 1
        
        nums = [bin(num)[2:] for num in nums]
        nums.sort(key=cmp_to_key(compare))

        ans = ''.join(nums)
        return int(ans, 2)
