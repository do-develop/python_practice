"""
# Method 1 - Brute Force O(N^2)
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i,j]

# Method 2 - Use 'in' O(N^2)
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i, n in enumerate(nums):
            complement = target - n

        if complement in nums[i+1:]:
            return nums.index(n), nums[i+1:].index(complement) + (i+1)

# Method 3 - Check the key value for the "target - first number" O(N)
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_map = {}
        #store key value in the dictionary
        for i, num in enumerate(nums):
            nums_map[num] = i

        for i, num in enumerate(nums):
            if target-num in nums_map and i != nums_map[target-num]:
                return nums.index(num), nums_map[target-num]

# Method 4 - Simplify method 3, O(N)
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_map = {}
        #store key value in the dictionary
        for i, num in enumerate(nums):
            if target-num in nums_map:
                return [nums_map[target-num], i]
            nums_map[num] = i
"""
from typing import List

# Method 5 - Move two pointers
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        left, right = 0, len(nums)-1
        while not left == right:
            # if two sum is bigger than the target move right-pointer to the left
            if nums[left] + nums[right] < target:
                left += 1
            # if two sum is smaller than the target move the left-pointer to the right
            elif nums[left] + nums[right] > target:
                right -= 1
            else:
                return left, right

obj = Solution()
nums = [2, 7, 11, 15, 16]
target = 17
print(obj.twoSum(nums, target))