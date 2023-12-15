class Solution:
    def getMaximumXor(self, nums: List[int], maximumBit: int) -> List[int]:
        k = 2 ** maximumBit - 1
        prefix = [nums[0]]
        for i in range(1, len(nums)):
            prefix.append(prefix[i - 1] ^ nums[i])
        
        ans = []
        for i in range(len(nums) - 1, -1, -1):
            ans.append(prefix[i] ^ k)
        return ans
