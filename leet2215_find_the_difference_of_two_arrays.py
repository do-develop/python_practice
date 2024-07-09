class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        answer = [[] for _ in range(2)]
        unique = set()

        for n in nums1:
            if n not in nums2:
                unique.add(n)
        answer[0] = list(unique)
        
        unique.clear()
        for n in nums2:
            if n not in nums1:
                unique.add(n)
        answer[1] = list(unique)

        return answer
