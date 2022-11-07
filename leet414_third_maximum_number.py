# from sortedcontainers import SortedSet

class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        # Approach - three pointers
        max1 = -inf
        max2 = -inf
        max3 = -inf
        
        for n in nums:
            if max1 == n or max2 == n or max3 == n:
                continue
            if max1 <= n:
                max3 = max2
                max2 = max1
                max1 = n
            elif max2 <= n:
                max3 = max2
                max2 = n
            elif max3 <= n:
                max3 = n
            
        if max3 == -inf:
            return max1
        return max3
    
        # Approach - SortedSet
        """
        sorted_nums = SortedSet()
        
        for n in nums:
            if n in sorted_nums:
                continue
            if len(sorted_nums) == 3:
                if sorted_nums[0] < n:
                    sorted_nums.discard(sorted_nums[0])
                    sorted_nums.add(n)
            else:
                sorted_nums.add(n)
                
        if len(sorted_nums) == 3:
            return sorted_nums[0]
    
        return sorted_nums[-1]
        """
