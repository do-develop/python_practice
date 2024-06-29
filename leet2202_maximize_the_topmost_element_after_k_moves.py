class Solution:
    def maximumTop(self, nums: List[int], k: int) -> int:
        # edge case - empty pile
        if len(nums) == 1 and k % 2 == 1:
            return -1
        
        # track the max element
        maxi = -1
        for i in range(min(len(nums), k - 1)):
            maxi = max(maxi, nums[i])

        if k < len(nums):
            maxi = max(maxi, nums[k]) # removing first k elements from the array if the kth element is greater
        
        return maxi
