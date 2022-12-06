class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # initialise with default value -1
        greater_map = {x: -1 for x in nums1}
        stack = []
        
        for num in nums2:
            while stack and stack[-1] < num:
                prev_num = stack.pop()
                if prev_num in greater_map:
                    # store the next great number in the map
                    greater_map[prev_num] = num
            stack.append(num)
            
        return [greater_map[x] for x in nums1]
