class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        count1, count2, ans = Counter(), Counter(), 0
        
        for n1, n2 in product(nums1, nums2):
            count1[n1 + n2] += 1
        
        for n3, n4 in product(nums3, nums4):
            count2[n3 + n4] += 1
        
        for val in count1:
            if -val in count2:
                ans += count1[val] * count2[-val]
            
        return ans
