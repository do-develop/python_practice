class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        '''
        nums.sort()
        indices = []
        for i in range(len(nums)):
            if nums[i] == target:
                indices.append(i)
        
        return indices
        '''
        # O(N) approach
        less = equal = 0
        for n in nums:
            if n < target:
                less += 1
            if n == target:
                equal += 1
        
        return list(range(less, less + equal))
