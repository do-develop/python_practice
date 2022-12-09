class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        res = [-1] * len(nums)
        stack = []
        greatest = float('-inf')
        
        for idx, num in enumerate(nums):
            while stack and nums[stack[-1]] < num:
                res[stack.pop()] = num
            stack.append(idx)
            greatest = max(greatest, num)
        # second pass to fix wrong entry (without circular property)
        # only until it reaches the largest one again
        for idx, num in enumerate(nums):
            while stack and nums[stack[-1]] < num:
                res[stack.pop()] = num
            if num == greatest:
                break
        return res
