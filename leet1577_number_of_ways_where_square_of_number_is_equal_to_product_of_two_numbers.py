class Solution:
    def numTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        d1 = collections.defaultdict(int)
        d2 = collections.defaultdict(int)
        res = 0

        for n1 in nums1:
            d1[n1 * n1] += 1
        for n2 in nums2:
            d2[n2 * n2] += 1
        for j in range(len(nums1) - 1):
            for k in range(j + 1, len(nums1)):
                res += d2[nums1[j] * nums1[k]]
        for j in range(len(nums2) - 1):
            for k in range(j + 1, len(nums2)):
                res += d1[nums2[j] * nums2[k]]

        return res    
        
