class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        presum = 0 # prefix sum
        dic = {0: 1}

        for i in range(len(nums)):
            presum += nums[i]
            count += dic.get(presum - k, 0)
            dic[presum] = dic.get(presum, 0) + 1
        
        return count
