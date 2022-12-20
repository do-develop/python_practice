class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        remainders = {0: -1} # remainder : index
        total = 0 

        # can detect subarray with sum value of multiple of k
        # by iterating the array once while checking the sum value
        # if the sum mod k == 0 there has been the subarray
        for idx, num in enumerate(nums):
            total += num
            rem = total % k
            if rem not in remainders:
                remainders[rem] = idx
            elif idx - remainders[rem] > 1:
                return True
        return False