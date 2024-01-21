class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        # instead of sorting linear tracking
        largest, seclargest = 0, 0
        smallest, secsmallest = float('inf'), float('inf')

        for n in nums:
            if n < smallest:
                secsmallest = smallest
                smallest = n
            elif n < secsmallest:
                secsmallest = n
            
            if n > largest:
                seclargest = largest
                largest = n
            elif n > seclargest:
                seclargest = n
            
        return (largest * seclargest) - (smallest * secsmallest)
