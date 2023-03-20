class Solution:
    def partitionDisjoint(self, nums: List[int]) -> int:
        # track max value so far
        # if an element is smaller than max so far
        # the value belongs to the left partition
        disjoint = 0 # disjointing position
        max_so_far = left_max= nums[0]
        for i in range(1, len(nums)):
            max_so_far = max(max_so_far, nums[i])
            if nums[i] < left_max: # value should be in left partition
                disjoint = i
                left_max = max_so_far
        return disjoint + 1 # because index starts from 0
